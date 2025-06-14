import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
import joblib

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            logging.info("Preparing preprocessing pipeline...")

            numeric_features = ['writing_score', 'reading_score']
            categorical_features = ['gender', 'race_ethnicity', 'parental_level_of_education',
                                    'lunch', 'test_preparation_course']

            # Numeric pipeline
            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])

            # Categorical pipeline
            cat_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown='ignore')),
                ('scaler', StandardScaler(with_mean=False))
            ])

            preprocessor = ColumnTransformer(transformers=[
                ('num', num_pipeline, numeric_features),
                ('cat', cat_pipeline, categorical_features)
            ])

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data for transformation")

            preprocessing_obj = self.get_data_transformer_object()

            target_column = 'math_score'
            input_features_train = train_df.drop(columns=[target_column])
            target_feature_train = train_df[target_column]

            input_features_test = test_df.drop(columns=[target_column])
            target_feature_test = test_df[target_column]

            input_features_train_arr = preprocessing_obj.fit_transform(input_features_train)
            input_features_test_arr = preprocessing_obj.transform(input_features_test)

            # Save the preprocessor for later use
            os.makedirs(os.path.dirname(self.config.preprocessor_obj_file_path), exist_ok=True)
            joblib.dump(preprocessing_obj, self.config.preprocessor_obj_file_path)

            logging.info("Preprocessing completed and object saved.")

            return (
                np.c_[input_features_train_arr, target_feature_train],
                np.c_[input_features_test_arr, target_feature_test],
                self.config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e, sys)
