  
  
  -- Select all columns from individual_carbon_footprint
SELECT
  *
FROM
  `argon-zoo-413112.climate_change_accelerator.individual_carbon_footprint` AS individual_carbon_footprint;
  
  
  -- Average Carbon Footprint by Country and Diet
SELECT
  individual_carbon_footprint.Country,
  individual_carbon_footprint.Diet,
  AVG(individual_carbon_footprint.Carbon_Footprint) AS Average_Carbon_Footprint
FROM
  `argon-zoo-413112.climate_change_accelerator.individual_carbon_footprint` AS individual_carbon_footprint
GROUP BY
  1,
  2;
  
  
  --Impact of Transportation on Carbon Footprint
SELECT
  Transportation,
  AVG(Carbon_Footprint) AS Avg_Footprint
FROM
  `climate_change_accelerator.individual_carbon_footprint`
GROUP BY
  Transportation
ORDER BY
  Avg_Footprint DESC;
  
  
  -- BigQueryML Linear Regression Model
CREATE OR REPLACE MODEL
  `climate_change_accelerator.carbon_footprint_model` OPTIONS(model_type='linear_reg',
    input_label_cols=['Carbon_Footprint']) AS
SELECT
  *
FROM
  `climate_change_accelerator.individual_carbon_footprint`;
  
  
  -- Model Evaluation
SELECT
  *
FROM
  ML.EVALUATE(MODEL `climate_change_accelerator.carbon_footprint_model`);
  
  
  -- Prediction
SELECT
  *
FROM
  ML.PREDICT(MODEL `climate_change_accelerator.carbon_footprint_model`,
    (
    SELECT
      'France' AS Country,
      55 AS Age,
      'Meat-based' AS Diet,
      'Bicycle' AS Transportation,
      'House' AS Housing));


-- Register the Model
ALTER MODEL IF EXISTS `climate_change_accelerator.carbon_footprint_model` SET OPTIONS (vertex_ai_model_id="carbon_footprint_model");
