import os

import yaml
from yaml.loader import SafeLoader


class Params:
    """
    Class that contains the parameters of the program.
    Loads the parameters from a yaml file or from a dictionary.
    """

    PARAMETER_KEYS = {
        "bootstrap_threshold": 0,
        "dist_threshold": 100,
        "window_size": 10,
        "step_size": 1,
        "data_names": ["Lat_end_dec_newick", "Long_start_dec_newick", "Depth_start_newick", "Windspeed_start_newick", "Windspeed_end_newick", "Watertemp_ground_newick", "O2-saturation_ground_newick"],
        "reference_gene_dir": "./datasets/2024",
        "reference_gene_file": "sequences2.fasta",
        "file_name": "./datasets/2024/data.csv",
        "specimen": "Field_id",
        "names": ["Field_id", "Lat_end_dec", "Long_start_dec", "Depth_start", "Windspeed_start", "Windspeed_end", "Watertemp_ground", "O2-saturation_ground"],
        "makeDebugFiles": True,
        "bootstrap_amount": 10,
        "alignment_method": "1",
        "distance_method": "0",
        "fit_method": "1",
        "tree_type": "1",
        "rate_similarity": 5,
        "method_similarity": "1",
    }

    @classmethod
    def load_from_file(cls, params_file=os.path.join(os.path.dirname(__file__), "params.yaml")):
        """
        Method that loads the parameters from a yaml file.

        args:
            params_file (str): the path to the yaml file
        """
        with open(params_file) as f:
            params = yaml.load(f, Loader=SafeLoader)
            cls.validate_and_set_params(params)

    @classmethod
    def update_from_dict(cls, params_content):
        """
        Method that updates the parameters from a dictionary.

        args:
            params_content (dict): the dictionary with the parameters
        """
        cls.validate_and_set_params(params_content)

    @classmethod
    def validate_and_set_params(cls, params_dict):
        """
        Method that validates and sets the parameters.

        args:
            params_dict (dict): the dictionary with the parameters
        """
        for key, value in params_dict.items():
            if key in cls.PARAMETER_KEYS:
                setattr(cls, key, value)
            else:
                raise ValueError(f"Invalid parameter: {key}")

        if hasattr(cls, "reference_gene_dir") and hasattr(cls, "reference_gene_file"):
            cls.reference_gene_filepath = os.path.join(cls.reference_gene_dir, cls.reference_gene_file)
        else:
            cls.reference_gene_filepath = None
