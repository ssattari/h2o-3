#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2OWord2vecEstimator(H2OEstimator):
    """
    Word2Vec

    """

    algo = "word2vec"
    supervised_learning = False
    _options_ = {'requires_training_frame': False}

    def __init__(self,
                 model_id=None,  # type: Optional[Union[None, str, H2OEstimator]]
                 training_frame=None,  # type: Optional[Union[None, str, H2OFrame]]
                 min_word_freq=5,  # type: int
                 word_model="skip_gram",  # type: Literal["skip_gram", "cbow"]
                 norm_model="hsm",  # type: Literal["hsm"]
                 vec_size=100,  # type: int
                 window_size=5,  # type: int
                 sent_sample_rate=0.001,  # type: float
                 init_learning_rate=0.025,  # type: float
                 epochs=5,  # type: int
                 pre_trained=None,  # type: Optional[Union[None, str, H2OFrame]]
                 max_runtime_secs=0.0,  # type: float
                 export_checkpoints_dir=None,  # type: Optional[str]
                 ):
        """
        :param model_id: Destination id for this model; auto-generated if not specified.
               Defaults to ``None``.
        :type model_id: Union[None, str, H2OEstimator], optional
        :param training_frame: Id of the training data frame.
               Defaults to ``None``.
        :type training_frame: Union[None, str, H2OFrame], optional
        :param min_word_freq: This will discard words that appear less than <int> times
               Defaults to ``5``.
        :type min_word_freq: int
        :param word_model: The word model to use (SkipGram or CBOW)
               Defaults to ``"skip_gram"``.
        :type word_model: Literal["skip_gram", "cbow"]
        :param norm_model: Use Hierarchical Softmax
               Defaults to ``"hsm"``.
        :type norm_model: Literal["hsm"]
        :param vec_size: Set size of word vectors
               Defaults to ``100``.
        :type vec_size: int
        :param window_size: Set max skip length between words
               Defaults to ``5``.
        :type window_size: int
        :param sent_sample_rate: Set threshold for occurrence of words. Those that appear with higher frequency in the
               training data
                               will be randomly down-sampled; useful range is (0, 1e-5)
               Defaults to ``0.001``.
        :type sent_sample_rate: float
        :param init_learning_rate: Set the starting learning rate
               Defaults to ``0.025``.
        :type init_learning_rate: float
        :param epochs: Number of training iterations to run
               Defaults to ``5``.
        :type epochs: int
        :param pre_trained: Id of a data frame that contains a pre-trained (external) word2vec model
               Defaults to ``None``.
        :type pre_trained: Union[None, str, H2OFrame], optional
        :param max_runtime_secs: Maximum allowed runtime in seconds for model training. Use 0 to disable.
               Defaults to ``0.0``.
        :type max_runtime_secs: float
        :param export_checkpoints_dir: Automatically export generated models to this directory.
               Defaults to ``None``.
        :type export_checkpoints_dir: str, optional
        """
        super(H2OWord2vecEstimator, self).__init__()
        self._parms = {}
        self._id = self._parms['model_id'] = model_id
        self.training_frame = training_frame
        self.min_word_freq = min_word_freq
        self.word_model = word_model
        self.norm_model = norm_model
        self.vec_size = vec_size
        self.window_size = window_size
        self.sent_sample_rate = sent_sample_rate
        self.init_learning_rate = init_learning_rate
        self.epochs = epochs
        self.pre_trained = pre_trained
        self.max_runtime_secs = max_runtime_secs
        self.export_checkpoints_dir = export_checkpoints_dir

    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``Union[None, str, H2OFrame]``.

        :examples:

        >>> job_titles = h2o.import_file(("https://s3.amazonaws.com/h2o-public-test-data/smalldata/craigslistJobTitles.csv"), 
        ...                               col_names = ["category", "jobtitle"], 
        ...                               col_types = ["string", "string"], 
        ...                               header = 1)
        >>> words = job_titles.tokenize(" ")
        >>> w2v_model = H2OWord2vecEstimator()
        >>> w2v_model.train(training_frame=words)
        >>> synonyms = w2v_model.find_synonyms("tutor", 3)
        >>> print(synonyms)
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        self._parms["training_frame"] = H2OFrame._validate(training_frame, 'training_frame')

    @property
    def min_word_freq(self):
        """
        This will discard words that appear less than <int> times

        Type: ``int``, defaults to ``5``.

        :examples:

        >>> job_titles = h2o.import_file(("https://s3.amazonaws.com/h2o-public-test-data/smalldata/craigslistJobTitles.csv"), 
        ...                               col_names = ["category", "jobtitle"], 
        ...                               col_types = ["string", "string"], 
        ...                               header = 1)
        >>> words = job_titles.tokenize(" ")
        >>> w2v_model = H2OWord2vecEstimator(epochs=1, min_word_freq=4)
        >>> w2v_model.train(training_frame=words)
        >>> synonyms = w2v_model.find_synonyms("teacher", 3)
        >>> print(synonyms)
        """
        return self._parms.get("min_word_freq")

    @min_word_freq.setter
    def min_word_freq(self, min_word_freq):
        assert_is_type(min_word_freq, None, int)
        self._parms["min_word_freq"] = min_word_freq

    @property
    def word_model(self):
        """
        The word model to use (SkipGram or CBOW)

        Type: ``Literal["skip_gram", "cbow"]``, defaults to ``"skip_gram"``.

        :examples:

        >>> job_titles = h2o.import_file(("https://s3.amazonaws.com/h2o-public-test-data/smalldata/craigslistJobTitles.csv"), 
        ...                               col_names = ["category", "jobtitle"], 
        ...                               col_types = ["string", "string"], 
        ...                               header = 1)
        >>> words = job_titles.tokenize(" ")
        >>> w2v_model = H2OWord2vecEstimator(epochs=3, word_model="skip_gram")
        >>> w2v_model.train(training_frame=words)
        >>> synonyms = w2v_model.find_synonyms("assistant", 3)
        >>> print(synonyms)
        """
        return self._parms.get("word_model")

    @word_model.setter
    def word_model(self, word_model):
        assert_is_type(word_model, None, Enum("skip_gram", "cbow"))
        self._parms["word_model"] = word_model

    @property
    def norm_model(self):
        """
        Use Hierarchical Softmax

        Type: ``Literal["hsm"]``, defaults to ``"hsm"``.

        :examples:

        >>> job_titles = h2o.import_file(("https://s3.amazonaws.com/h2o-public-test-data/smalldata/craigslistJobTitles.csv"), 
        ...                               col_names = ["category", "jobtitle"], 
        ...                               col_types = ["string", "string"], 
        ...                               header = 1)
        >>> words = job_titles.tokenize(" ")
        >>> w2v_model = H2OWord2vecEstimator(epochs=1, norm_model="hsm")
        >>> w2v_model.train(training_frame=words)
        >>> synonyms = w2v_model.find_synonyms("teacher", 3)
        >>> print(synonyms)
        """
        return self._parms.get("norm_model")

    @norm_model.setter
    def norm_model(self, norm_model):
        assert_is_type(norm_model, None, Enum("hsm"))
        self._parms["norm_model"] = norm_model

    @property
    def vec_size(self):
        """
        Set size of word vectors

        Type: ``int``, defaults to ``100``.

        :examples:

        >>> job_titles = h2o.import_file(("https://s3.amazonaws.com/h2o-public-test-data/smalldata/craigslistJobTitles.csv"), 
        ...                               col_names = ["category", "jobtitle"], 
        ...                               col_types = ["string", "string"], 
        ...                               header = 1)
        >>> words = job_titles.tokenize(" ")
        >>> w2v_model = H2OWord2vecEstimator(epochs=3, vec_size=50)
        >>> w2v_model.train(training_frame=words)
        >>> synonyms = w2v_model.find_synonyms("tutor", 3)
        >>> print(synonyms)
        """
        return self._parms.get("vec_size")

    @vec_size.setter
    def vec_size(self, vec_size):
        assert_is_type(vec_size, None, int)
        self._parms["vec_size"] = vec_size

    @property
    def window_size(self):
        """
        Set max skip length between words

        Type: ``int``, defaults to ``5``.

        :examples:

        >>> job_titles = h2o.import_file(("https://s3.amazonaws.com/h2o-public-test-data/smalldata/craigslistJobTitles.csv"), 
        ...                               col_names = ["category", "jobtitle"], 
        ...                               col_types = ["string", "string"], 
        ...                               header = 1)
        >>> words = job_titles.tokenize(" ")
        >>> w2v_model = H2OWord2vecEstimator(epochs=3, window_size=2)
        >>> w2v_model.train(training_frame=words)
        >>> synonyms = w2v_model.find_synonyms("teacher", 3)
        >>> print(synonyms)
        """
        return self._parms.get("window_size")

    @window_size.setter
    def window_size(self, window_size):
        assert_is_type(window_size, None, int)
        self._parms["window_size"] = window_size

    @property
    def sent_sample_rate(self):
        """
        Set threshold for occurrence of words. Those that appear with higher frequency in the training data
                        will be randomly down-sampled; useful range is (0, 1e-5)

        Type: ``float``, defaults to ``0.001``.

        :examples:

        >>> job_titles = h2o.import_file(("https://s3.amazonaws.com/h2o-public-test-data/smalldata/craigslistJobTitles.csv"), 
        ...                               col_names = ["category", "jobtitle"], 
        ...                               col_types = ["string", "string"], 
        ...                               header = 1)
        >>> words = job_titles.tokenize(" ")
        >>> w2v_model = H2OWord2vecEstimator(epochs=1, sent_sample_rate=0.01)
        >>> w2v_model.train(training_frame=words)
        >>> synonyms = w2v_model.find_synonyms("teacher", 3)
        >>> print(synonyms)
        """
        return self._parms.get("sent_sample_rate")

    @sent_sample_rate.setter
    def sent_sample_rate(self, sent_sample_rate):
        assert_is_type(sent_sample_rate, None, float)
        self._parms["sent_sample_rate"] = sent_sample_rate

    @property
    def init_learning_rate(self):
        """
        Set the starting learning rate

        Type: ``float``, defaults to ``0.025``.

        :examples:

        >>> job_titles = h2o.import_file(("https://s3.amazonaws.com/h2o-public-test-data/smalldata/craigslistJobTitles.csv"), 
        ...                               col_names = ["category", "jobtitle"], 
        ...                               col_types = ["string", "string"], 
        ...                               header = 1)
        >>> words = job_titles.tokenize(" ")
        >>> w2v_model = H2OWord2vecEstimator(epochs=3, init_learning_rate=0.05)
        >>> w2v_model.train(training_frame=words)
        >>> synonyms = w2v_model.find_synonyms("assistant", 3)
        >>> print(synonyms)
        """
        return self._parms.get("init_learning_rate")

    @init_learning_rate.setter
    def init_learning_rate(self, init_learning_rate):
        assert_is_type(init_learning_rate, None, float)
        self._parms["init_learning_rate"] = init_learning_rate

    @property
    def epochs(self):
        """
        Number of training iterations to run

        Type: ``int``, defaults to ``5``.

        :examples:

        >>> job_titles = h2o.import_file(("https://s3.amazonaws.com/h2o-public-test-data/smalldata/craigslistJobTitles.csv"), 
        ...                               col_names = ["category", "jobtitle"], 
        ...                               col_types = ["string", "string"], 
        ...                               header = 1)
        >>> words = job_titles.tokenize(" ")
        >>> w2v_model = H2OWord2vecEstimator(sent_sample_rate = 0.0, epochs = 10)
        >>> w2v_model.train(training_frame=words)
        >>> synonyms = w2v_model.find_synonyms("teacher", count = 5)
        >>> print(synonyms)
        >>>
        >>> w2v_model2 = H2OWord2vecEstimator(sent_sample_rate = 0.0, epochs = 1)
        >>> w2v_model2.train(training_frame=words)
        >>> synonyms2 = w2v_model2.find_synonyms("teacher", 3)
        >>> print(synonyms2)
        """
        return self._parms.get("epochs")

    @epochs.setter
    def epochs(self, epochs):
        assert_is_type(epochs, None, int)
        self._parms["epochs"] = epochs

    @property
    def pre_trained(self):
        """
        Id of a data frame that contains a pre-trained (external) word2vec model

        Type: ``Union[None, str, H2OFrame]``.

        :examples:

        >>> words = h2o.create_frame(rows=1000,cols=1,
        ...                          string_fraction=1.0,
        ...                          missing_fraction=0.0)
        >>> embeddings = h2o.create_frame(rows=1000,cols=100,
        ...                               real_fraction=1.0,
        ...                               missing_fraction=0.0)
        >>> word_embeddings = words.cbind(embeddings)
        >>> w2v_model = H2OWord2vecEstimator(pre_trained=word_embeddings)
        >>> w2v_model.train(training_frame=word_embeddings)
        >>> model_id = w2v_model.model_id
        >>> model = h2o.get_model(model_id)
        """
        return self._parms.get("pre_trained")

    @pre_trained.setter
    def pre_trained(self, pre_trained):
        pt = self._parms["pre_trained"] = H2OFrame._validate(pre_trained, 'pre_trained')
        if pt is not None:
            self.vec_size = H2OWord2vecEstimator._determine_vec_size(pt)

    @property
    def max_runtime_secs(self):
        """
        Maximum allowed runtime in seconds for model training. Use 0 to disable.

        Type: ``float``, defaults to ``0.0``.

        :examples:

        >>> job_titles = h2o.import_file(("https://s3.amazonaws.com/h2o-public-test-data/smalldata/craigslistJobTitles.csv"), 
        ...                               col_names = ["category", "jobtitle"], 
        ...                               col_types = ["string", "string"], 
        ...                               header = 1)
        >>> words = job_titles.tokenize(" ")
        >>> w2v_model = H2OWord2vecEstimator(epochs=1, max_runtime_secs=10)
        >>> w2v_model.train(training_frame=words)
        >>> synonyms = w2v_model.find_synonyms("tutor", 3)
        >>> print(synonyms)
        """
        return self._parms.get("max_runtime_secs")

    @max_runtime_secs.setter
    def max_runtime_secs(self, max_runtime_secs):
        assert_is_type(max_runtime_secs, None, numeric)
        self._parms["max_runtime_secs"] = max_runtime_secs

    @property
    def export_checkpoints_dir(self):
        """
        Automatically export generated models to this directory.

        Type: ``str``.

        :examples:

        >>> import tempfile
        >>> from os import listdir
        >>> job_titles = h2o.import_file(("https://s3.amazonaws.com/h2o-public-test-data/smalldata/craigslistJobTitles.csv"), 
        ...                               col_names = ["category", "jobtitle"], 
        ...                               col_types = ["string", "string"], 
        ...                               header = 1)
        >>> checkpoints_dir = tempfile.mkdtemp()
        >>> words = job_titles.tokenize(" ")
        >>> w2v_model = H2OWord2vecEstimator(epochs=1,
        ...                                  max_runtime_secs=10,
        ...                                  export_checkpoints_dir=checkpoints_dir)
        >>> w2v_model.train(training_frame=words)
        >>> len(listdir(checkpoints_dir))
        """
        return self._parms.get("export_checkpoints_dir")

    @export_checkpoints_dir.setter
    def export_checkpoints_dir(self, export_checkpoints_dir):
        assert_is_type(export_checkpoints_dir, None, str)
        self._parms["export_checkpoints_dir"] = export_checkpoints_dir

    @staticmethod
    def from_external(external=H2OFrame):
        """
        Creates new H2OWord2vecEstimator based on an external model.

        :param external: H2OFrame with an external model
        :return: H2OWord2vecEstimator instance representing the external model

        :examples:

        >>> words = h2o.create_frame(rows=10, cols=1,
        ...                          string_fraction=1.0,
        ...                          missing_fraction=0.0)
        >>> embeddings = h2o.create_frame(rows=10, cols=100,
        ...                               real_fraction=1.0,
        ...                               missing_fraction=0.0)
        >>> word_embeddings = words.cbind(embeddings)
        >>> w2v_model = H2OWord2vecEstimator.from_external(external=word_embeddings)
        """
        w2v_model = H2OWord2vecEstimator(pre_trained=external)
        w2v_model.train()
        return w2v_model

    @staticmethod
    def _determine_vec_size(pre_trained):
        """
        Determines vec_size for a pre-trained model after basic model verification.
        """
        first_column = pre_trained.types[pre_trained.columns[0]]

        if first_column != 'string':
            raise H2OValueError("First column of given pre_trained model %s is required to be a String",
                                pre_trained.frame_id)

        if list(pre_trained.types.values()).count('string') > 1:
            raise H2OValueError("There are multiple columns in given pre_trained model %s with a String type.",
                                pre_trained.frame_id)

        return pre_trained.dim[1] - 1

