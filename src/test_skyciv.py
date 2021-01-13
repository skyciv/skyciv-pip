import skyciv

# THIS HAS NOT BEEN IMPLEMENTED YET.

data = {
    "auth": {
        "username": "YOUR_SKYCIV_ACCOUNT",
        "key": "YOUR_SKYCIV_API_KEY"
    },
    "functions": [
        {
            'function': 'S3D.session.start',
            'arguments': {}
        },
        {
            'function': 'S3D.model.set',
            'arguments': {
                's3d_model': {
        "settings": {
            "vertical_axis": "Z",
            "units": {
                "length": "m",
                "section_length": "mm",
                "material_strength": "mpa",
                "density": "kg/m3",
                "force": "kn",
                "moment": "kn-m",
                "pressure": "kpa",
                "mass": "kg",
                "translation": "mm",
                "stress": "mpa"
            }
        },
        "nodes": {
            "1": {
                "x": 0,
                "y": 0,
                "z": 0
            },
            "2": {
                "x": 5,
                "y": 0,
                "z": 0
            }
        },
        "members": {
            "1": {
                "node_A": 1,
                "node_B": 2,
                "section_id": 1
            }
        },
        "sections": {
            "1": {
                "load_section": [
                    "Australian", 
                    "Steel (250 Grade)", 
                    "Circular hollow sections (350)", 
                    "457x6.4 CHS"
                    ],
                "material_id": 1
            }
        },
        "materials": {
            "1": {
                "name": "Structural Steel",
                "density": 7850,
                "elasticity_modulus": 200000,
                "poissons_ratio": 0.27,
                "yield_strength": 350,
                "ultimate_strength": 470,
                "class": "steel"
            }
        },
        "supports": {
            "1": {
                "node": 1,
                "restraint_code": "FFFFFF"
            }
        },
        "point_loads": {
            "1": {
                "type": "n",
                "node": 2,
                "x_mag": 0,
                "y_mag": 0,
                "z_mag": -10,
                "load_group": "Live_PL"
            },
            "2": {
                "type": "M",
                "member": 1,
                "position": 80,
                "x_mag": 0,
                "y_mag": 0,
                "z_mag": -3,
                "load_group": "Live_PL"
            }
        },
        "distributed_loads": {
            "1": {
                "member": 1,
                "x_mag_A": 0,
                "y_mag_A": 0,
                "z_mag_A": -10,
                "x_mag_B": 0,
                "y_mag_B": 0,
                "z_mag_B": -10,
                "position_A": 0,
                "position_B": 100,
                "load_group": "Live_Dist_Load",
                "axes": "global"
            }
        },
        "self_weight": {
            "1": {
                "LG": "SW1",
                "x": 0,
                "y": 0,
                "z": -1
            }
        }
            }
        },
        {
            'function': "S3D.model.solve",
            'arguments': {
                analysis_type: 'nonlinear',
                repair_model: true
            },
        }
    ]
}

def test_skyciv_request_no_options_empty_data():
    assert skyciv.request({}) == Exception()

def test_skyciv_request_http_empty_data():
    options = {
        "http_or_https": "http",
        "version": 3,
    }
    assert skyciv.request({}}, options);

def test_skyciv_request_https_empty_data():
    options = {
        "http_or_https": "https",
        "version": 3,
    }
    assert skyciv.request({}}, options);

def test_skyciv_request_https_with_data():
    options = {
        "http_or_https": "https",
        "version": 3,
    }
    assert skyciv.request(data, options);