SELECT * FROM top100csvfile;
SELECT * FROM top100csvfile WHERE country = 'United States'
SELECT * FROM top100csvfile ORDER BY influence_score
SELECT country, COUNT(country) FROM top100csvfile GROUP BY country
