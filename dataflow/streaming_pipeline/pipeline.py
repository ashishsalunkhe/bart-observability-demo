import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json

class ParseBARTRecord(beam.DoFn):
    def process(self, element):
        record = json.loads(element.decode('utf-8'))
        try:
            estimates = record['etd'][0]['estimate']
            for e in estimates:
                yield {
                    'station': record['abbr'],
                    'destination': record['etd'][0]['destination'],
                    'platform': e.get('platform'),
                    'direction': e.get('direction'),
                    'minutes': int(e['minutes']) if e['minutes'].isdigit() else -1,
                    'length': int(e.get('length', -1)),
                    'color': e.get('color')
                }
        except Exception as e:
            yield beam.pvalue.TaggedOutput('errors', {'error': str(e), 'data': record})

def run(argv=None):
    options = PipelineOptions(streaming=True, save_main_session=True)
    with beam.Pipeline(options=options) as p:
        records = (
            p
            | 'Read from PubSub' >> beam.io.ReadFromPubSub(topic='projects/your-project-id/topics/bart-etd')
            | 'Parse ETD Records' >> beam.ParDo(ParseBARTRecord()).with_outputs('errors', main='valid')
        )

        records.valid | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
            table='your-project-id:your_dataset.bart_etd',
            schema='station:STRING,destination:STRING,platform:STRING,direction:STRING,minutes:INTEGER,length:INTEGER,color:STRING',
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
        )

        records.errors | 'Log Errors' >> beam.Map(print)
