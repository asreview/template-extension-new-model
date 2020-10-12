# Template for extending ASReview with new model

ASReview has support for extensions, which enable you to seemlessly integrate
your own programs with the ASReview framework. These extensions can extend the
software with new models, qurey strategies, balance strategies, and feature
extraction techniques. This template can be used to write such an extension
(add a new SKLearn naive Bayes classifier with default settings in this case).

See https://asreview.readthedocs.io/en/latest/extensions_dev.html for more
information on writing extensions.

## Installation

Install the new classifier with:

```bash
pip install git@github.com:asreview/template-extension-new-model.git
```

## Usage

Use the new classifier `nd_example` is defined in
[`asreviewcontrib/models/nb_defau
lt_param.py`](asreviewcontrib/models/nb_default_param.py) and can be used in a
simulation

```bash
asreview simulate example_data_file.csv -m nb_example
```

## License

MIT license
