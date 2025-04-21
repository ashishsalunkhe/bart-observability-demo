SELECT
  station,
  AVG(minutes) AS avg_wait_minutes,
  COUNT(*) AS trip_count
FROM `your-project-id.bart_data.bart_etd`
WHERE minutes >= 0
GROUP BY station
ORDER BY avg_wait_minutes DESC
