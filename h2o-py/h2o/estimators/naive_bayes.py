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


class H2ONaiveBayesEstimator(H2OEstimator):
    """
    Naive Bayes

    The naive Bayes classifier assumes independence between predictor variables
    conditional on the response, and a Gaussian distribution of numeric predictors with
    mean and standard deviation computed from the training dataset. When building a naive
    Bayes classifier, every row in the training dataset that contains at least one NA will
    be skipped completely. If the test dataset has missing values, then those predictors
    are omitted in the probability calculation during prediction.
    """

    algo = "naivebayes"
    supervised_learning = True

    def __init__(self,
                 model_id=None,  # type: Optional[Union[None, str, H2OEstimator]]
                 nfolds=0,  # type: int
                 seed=-1,  # type: int
                 fold_assignment="auto",  # type: Literal["auto", "random", "modulo", "stratified"]
                 fold_column=None,  # type: Optional[str]
                 keep_cross_validation_models=True,  # type: bool
                 keep_cross_validation_predictions=False,  # type: bool
                 keep_cross_validation_fold_assignment=False,  # type: bool
                 training_frame=None,  # type: Optional[Union[None, str, H2OFrame]]
                 validation_frame=None,  # type: Optional[Union[None, str, H2OFrame]]
                 response_column=None,  # type: Optional[str]
                 ignored_columns=None,  # type: Optional[List[str]]
                 ignore_const_cols=True,  # type: bool
                 score_each_iteration=False,  # type: bool
                 balance_classes=False,  # type: bool
                 class_sampling_factors=None,  # type: Optional[List[float]]
                 max_after_balance_size=5.0,  # type: float
                 max_confusion_matrix_size=20,  # type: int
                 laplace=0.0,  # type: float
                 min_sdev=0.001,  # type: float
                 eps_sdev=0.0,  # type: float
                 min_prob=0.001,  # type: float
                 eps_prob=0.0,  # type: float
                 compute_metrics=True,  # type: bool
                 max_runtime_secs=0.0,  # type: float
                 export_checkpoints_dir=None,  # type: Optional[str]
                 gainslift_bins=-1,  # type: int
                 auc_type="auto",  # type: Literal["auto", "none", "macro_ovr", "weighted_ovr", "macro_ovo", "weighted_ovo"]
                 ):
        """
        :param model_id: Destination id for this model; auto-generated if not specified.
               Defaults to ``None``.
        :type model_id: Union[None, str, H2OEstimator], optional
        :param nfolds: Number of folds for K-fold cross-validation (0 to disable or >= 2).
               Defaults to ``0``.
        :type nfolds: int
        :param seed: Seed for pseudo random number generator (only used for cross-validation and
               fold_assignment="Random" or "AUTO")
               Defaults to ``-1``.
        :type seed: int
        :param fold_assignment: Cross-validation fold assignment scheme, if fold_column is not specified. The
               'Stratified' option will stratify the folds based on the response variable, for classification problems.
               Defaults to ``"auto"``.
        :type fold_assignment: Literal["auto", "random", "modulo", "stratified"]
        :param fold_column: Column with cross-validation fold index assignment per observation.
               Defaults to ``None``.
        :type fold_column: str, optional
        :param keep_cross_validation_models: Whether to keep the cross-validation models.
               Defaults to ``True``.
        :type keep_cross_validation_models: bool
        :param keep_cross_validation_predictions: Whether to keep the predictions of the cross-validation models.
               Defaults to ``False``.
        :type keep_cross_validation_predictions: bool
        :param keep_cross_validation_fold_assignment: Whether to keep the cross-validation fold assignment.
               Defaults to ``False``.
        :type keep_cross_validation_fold_assignment: bool
        :param training_frame: Id of the training data frame.
               Defaults to ``None``.
        :type training_frame: Union[None, str, H2OFrame], optional
        :param validation_frame: Id of the validation data frame.
               Defaults to ``None``.
        :type validation_frame: Union[None, str, H2OFrame], optional
        :param response_column: Response variable column.
               Defaults to ``None``.
        :type response_column: str, optional
        :param ignored_columns: Names of columns to ignore for training.
               Defaults to ``None``.
        :type ignored_columns: List[str], optional
        :param ignore_const_cols: Ignore constant columns.
               Defaults to ``True``.
        :type ignore_const_cols: bool
        :param score_each_iteration: Whether to score during each iteration of model training.
               Defaults to ``False``.
        :type score_each_iteration: bool
        :param balance_classes: Balance training data class counts via over/under-sampling (for imbalanced data).
               Defaults to ``False``.
        :type balance_classes: bool
        :param class_sampling_factors: Desired over/under-sampling ratios per class (in lexicographic order). If not
               specified, sampling factors will be automatically computed to obtain class balance during training.
               Requires balance_classes.
               Defaults to ``None``.
        :type class_sampling_factors: List[float], optional
        :param max_after_balance_size: Maximum relative size of the training data after balancing class counts (can be
               less than 1.0). Requires balance_classes.
               Defaults to ``5.0``.
        :type max_after_balance_size: float
        :param max_confusion_matrix_size: [Deprecated] Maximum size (# classes) for confusion matrices to be printed in
               the Logs
               Defaults to ``20``.
        :type max_confusion_matrix_size: int
        :param laplace: Laplace smoothing parameter
               Defaults to ``0.0``.
        :type laplace: float
        :param min_sdev: Min. standard deviation to use for observations with not enough data
               Defaults to ``0.001``.
        :type min_sdev: float
        :param eps_sdev: Cutoff below which standard deviation is replaced with min_sdev
               Defaults to ``0.0``.
        :type eps_sdev: float
        :param min_prob: Min. probability to use for observations with not enough data
               Defaults to ``0.001``.
        :type min_prob: float
        :param eps_prob: Cutoff below which probability is replaced with min_prob
               Defaults to ``0.0``.
        :type eps_prob: float
        :param compute_metrics: Compute metrics on training data
               Defaults to ``True``.
        :type compute_metrics: bool
        :param max_runtime_secs: Maximum allowed runtime in seconds for model training. Use 0 to disable.
               Defaults to ``0.0``.
        :type max_runtime_secs: float
        :param export_checkpoints_dir: Automatically export generated models to this directory.
               Defaults to ``None``.
        :type export_checkpoints_dir: str, optional
        :param gainslift_bins: Gains/Lift table number of bins. 0 means disabled.. Default value -1 means automatic
               binning.
               Defaults to ``-1``.
        :type gainslift_bins: int
        :param auc_type: Set default multinomial AUC type.
               Defaults to ``"auto"``.
        :type auc_type: Literal["auto", "none", "macro_ovr", "weighted_ovr", "macro_ovo", "weighted_ovo"]
        """
        super(H2ONaiveBayesEstimator, self).__init__()
        self._parms = {}
        self._id = self._parms['model_id'] = model_id
        self.nfolds = nfolds
        self.seed = seed
        self.fold_assignment = fold_assignment
        self.fold_column = fold_column
        self.keep_cross_validation_models = keep_cross_validation_models
        self.keep_cross_validation_predictions = keep_cross_validation_predictions
        self.keep_cross_validation_fold_assignment = keep_cross_validation_fold_assignment
        self.training_frame = training_frame
        self.validation_frame = validation_frame
        self.response_column = response_column
        self.ignored_columns = ignored_columns
        self.ignore_const_cols = ignore_const_cols
        self.score_each_iteration = score_each_iteration
        self.balance_classes = balance_classes
        self.class_sampling_factors = class_sampling_factors
        self.max_after_balance_size = max_after_balance_size
        self.max_confusion_matrix_size = max_confusion_matrix_size
        self.laplace = laplace
        self.min_sdev = min_sdev
        self.eps_sdev = eps_sdev
        self.min_prob = min_prob
        self.eps_prob = eps_prob
        self.compute_metrics = compute_metrics
        self.max_runtime_secs = max_runtime_secs
        self.export_checkpoints_dir = export_checkpoints_dir
        self.gainslift_bins = gainslift_bins
        self.auc_type = auc_type

    @property
    def nfolds(self):
        """
        Number of folds for K-fold cross-validation (0 to disable or >= 2).

        Type: ``int``, defaults to ``0``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response = "economy_20mpg"
        >>> cars_nb = H2ONaiveBayesEstimator(nfolds=5,
        ...                                  seed=1234)
        >>> cars_nb.train(x=predictors,
        ...               y=response,
        ...               training_frame=cars)
        >>> cars_nb.auc()
        """
        return self._parms.get("nfolds")

    @nfolds.setter
    def nfolds(self, nfolds):
        assert_is_type(nfolds, None, int)
        self._parms["nfolds"] = nfolds

    @property
    def seed(self):
        """
        Seed for pseudo random number generator (only used for cross-validation and fold_assignment="Random" or "AUTO")

        Type: ``int``, defaults to ``-1``.

        :examples:

        >>> airlines= h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip")
        >>> airlines["Year"] = airlines["Year"].asfactor()
        >>> airlines["Month"] = airlines["Month"].asfactor()
        >>> airlines["DayOfWeek"] = airlines["DayOfWeek"].asfactor()
        >>> airlines["Cancelled"] = airlines["Cancelled"].asfactor()
        >>> airlines['FlightNum'] = airlines['FlightNum'].asfactor()
        >>> predictors = ["Origin", "Dest", "Year", "UniqueCarrier",
        ...               "DayOfWeek", "Month", "Distance", "FlightNum"]
        >>> response = "IsDepDelayed"
        >>> train, valid= airlines.split_frame(ratios=[.8], seed=1234)
        >>> nb_w_seed = H2ONaiveBayesEstimator(seed=1234)
        >>> nb_w_seed.train(x=predictors,
        ...                 y=response,
        ...                 training_frame=train,
        ...                  validation_frame=valid)
        >>> nb_wo_seed = H2ONaiveBayesEstimator()
        >>> nb_wo_seed.train(x=predictors,
        ...                  y=response,
        ...                  training_frame=train,
        ...                  validation_frame=valid)
        >>> nb_w_seed.auc()
        >>> nb_wo_seed.auc()
        """
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed

    @property
    def fold_assignment(self):
        """
        Cross-validation fold assignment scheme, if fold_column is not specified. The 'Stratified' option will stratify
        the folds based on the response variable, for classification problems.

        Type: ``Literal["auto", "random", "modulo", "stratified"]``, defaults to ``"auto"``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response = "cylinders"
        >>> cars_nb = H2ONaiveBayesEstimator(fold_assignment="Random",
        ...                                  nfolds=5,
        ...                                  seed=1234)
        >>> response = "economy_20mpg"
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> cars_nb.train(x=predictors, y=response, training_frame=cars)
        >>> cars_nb.auc()
        """
        return self._parms.get("fold_assignment")

    @fold_assignment.setter
    def fold_assignment(self, fold_assignment):
        assert_is_type(fold_assignment, None, Enum("auto", "random", "modulo", "stratified"))
        self._parms["fold_assignment"] = fold_assignment

    @property
    def fold_column(self):
        """
        Column with cross-validation fold index assignment per observation.

        Type: ``str``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response = "economy_20mpg"
        >>> fold_numbers = cars.kfold_column(n_folds=5, seed=1234)
        >>> fold_numbers.set_names(["fold_numbers"])
        >>> cars = cars.cbind(fold_numbers)
        >>> cars_nb = H2ONaiveBayesEstimator(seed=1234)
        >>> cars_nb.train(x=predictors,
        ...               y=response,
        ...               training_frame=cars,
        ...               fold_column="fold_numbers")
        >>> cars_nb.auc()
        """
        return self._parms.get("fold_column")

    @fold_column.setter
    def fold_column(self, fold_column):
        assert_is_type(fold_column, None, str)
        self._parms["fold_column"] = fold_column

    @property
    def keep_cross_validation_models(self):
        """
        Whether to keep the cross-validation models.

        Type: ``bool``, defaults to ``True``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response = "economy_20mpg"
        >>> train, valid = cars.split_frame(ratios=[.8], seed=1234)
        >>> cars_nb = H2ONaiveBayesEstimator(keep_cross_validation_models=True,
        ...                                  nfolds=5,
        ...                                  seed=1234)
        >>> cars_nb.train(x=predictors,
        ...               y=response,
        ...               training_frame=train)
        >>> cars_nb.cross_validation_models()
        """
        return self._parms.get("keep_cross_validation_models")

    @keep_cross_validation_models.setter
    def keep_cross_validation_models(self, keep_cross_validation_models):
        assert_is_type(keep_cross_validation_models, None, bool)
        self._parms["keep_cross_validation_models"] = keep_cross_validation_models

    @property
    def keep_cross_validation_predictions(self):
        """
        Whether to keep the predictions of the cross-validation models.

        Type: ``bool``, defaults to ``False``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response = "economy_20mpg"
        >>> train, valid = cars.split_frame(ratios=[.8], seed=1234)
        >>> cars_nb = H2ONaiveBayesEstimator(keep_cross_validation_predictions=True,
        ...                                  nfolds=5,
        ...                                  seed=1234)
        >>> cars_nb.train(x=predictors,
        ...               y=response,
        ...               training_frame=train)
        >>> cars_nb.cross_validation_predictions()
        """
        return self._parms.get("keep_cross_validation_predictions")

    @keep_cross_validation_predictions.setter
    def keep_cross_validation_predictions(self, keep_cross_validation_predictions):
        assert_is_type(keep_cross_validation_predictions, None, bool)
        self._parms["keep_cross_validation_predictions"] = keep_cross_validation_predictions

    @property
    def keep_cross_validation_fold_assignment(self):
        """
        Whether to keep the cross-validation fold assignment.

        Type: ``bool``, defaults to ``False``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response = "economy_20mpg"
        >>> train, valid = cars.split_frame(ratios=[.8], seed=1234)
        >>> cars_nb = H2ONaiveBayesEstimator(keep_cross_validation_fold_assignment=True,
        ...                                  nfolds=5,
        ...                                  seed=1234)
        >>> cars_nb.train(x=predictors,
        ...               y=response,
        ...               training_frame=train)
        >>> cars_nb.cross_validation_fold_assignment()
        """
        return self._parms.get("keep_cross_validation_fold_assignment")

    @keep_cross_validation_fold_assignment.setter
    def keep_cross_validation_fold_assignment(self, keep_cross_validation_fold_assignment):
        assert_is_type(keep_cross_validation_fold_assignment, None, bool)
        self._parms["keep_cross_validation_fold_assignment"] = keep_cross_validation_fold_assignment

    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``Union[None, str, H2OFrame]``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response = "economy_20mpg"
        >>> train, valid = cars.split_frame(ratios=[.8], seed=1234)
        >>> cars_nb = H2ONaiveBayesEstimator()
        >>> cars_nb.train(x=predictors,
        ...               y=response,
        ...               training_frame=train,
        ...               validation_frame=valid)
        >>> cars_nb.auc()
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        self._parms["training_frame"] = H2OFrame._validate(training_frame, 'training_frame')

    @property
    def validation_frame(self):
        """
        Id of the validation data frame.

        Type: ``Union[None, str, H2OFrame]``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response = "economy_20mpg"
        >>> train, valid = cars.split_frame(ratios=[.8], seed=1234)
        >>> cars_nb = H2ONaiveBayesEstimator()
        >>> cars_nb.train(x=predictors,
        ...               y=response,
        ...               training_frame=train,
        ...               validation_frame=valid)
        >>> cars_nb.auc()
        """
        return self._parms.get("validation_frame")

    @validation_frame.setter
    def validation_frame(self, validation_frame):
        self._parms["validation_frame"] = H2OFrame._validate(validation_frame, 'validation_frame')

    @property
    def response_column(self):
        """
        Response variable column.

        Type: ``str``.
        """
        return self._parms.get("response_column")

    @response_column.setter
    def response_column(self, response_column):
        assert_is_type(response_column, None, str)
        self._parms["response_column"] = response_column

    @property
    def ignored_columns(self):
        """
        Names of columns to ignore for training.

        Type: ``List[str]``.
        """
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns

    @property
    def ignore_const_cols(self):
        """
        Ignore constant columns.

        Type: ``bool``, defaults to ``True``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response = "economy_20mpg"
        >>> cars["const_1"] = 6
        >>> cars["const_2"] = 7
        >>> train, valid = cars.split_frame(ratios=[.8], seed=1234)
        >>> cars_nb = H2ONaiveBayesEstimator(seed=1234,
        ...                                  ignore_const_cols=True)
        >>> cars_nb.train(x=predictors,
        ...               y=response,
        ...               training_frame=train,
        ...               validation_frame=valid)
        >>> cars_nb.auc()
        """
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols

    @property
    def score_each_iteration(self):
        """
        Whether to score during each iteration of model training.

        Type: ``bool``, defaults to ``False``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response = "economy_20mpg"
        >>> train, valid = cars.split_frame(ratios=[.8], seed=1234)
        >>> cars_nb = H2ONaiveBayesEstimator(score_each_iteration=True,
        ...                                  seed=1234)
        >>> cars_nb.train(x=predictors,
        ...               y=response,
        ...               training_frame=train,
        ...               validation_frame=valid)
        >>> cars_nb.auc()
        """
        return self._parms.get("score_each_iteration")

    @score_each_iteration.setter
    def score_each_iteration(self, score_each_iteration):
        assert_is_type(score_each_iteration, None, bool)
        self._parms["score_each_iteration"] = score_each_iteration

    @property
    def balance_classes(self):
        """
        Balance training data class counts via over/under-sampling (for imbalanced data).

        Type: ``bool``, defaults to ``False``.

        :examples:

        >>> iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        >>> iris_nb = H2ONaiveBayesEstimator(balance_classes=False,
        ...                                  nfolds=3,
        ...                                  seed=1234)
        >>> iris_nb.train(x=list(range(4)),
        ...               y=4,
        ...               training_frame=iris)
        >>> iris_nb.mse()
        """
        return self._parms.get("balance_classes")

    @balance_classes.setter
    def balance_classes(self, balance_classes):
        assert_is_type(balance_classes, None, bool)
        self._parms["balance_classes"] = balance_classes

    @property
    def class_sampling_factors(self):
        """
        Desired over/under-sampling ratios per class (in lexicographic order). If not specified, sampling factors will
        be automatically computed to obtain class balance during training. Requires balance_classes.

        Type: ``List[float]``.

        :examples:

        >>> covtype = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/covtype/covtype.20k.data")
        >>> covtype[54] = covtype[54].asfactor()
        >>> sample_factors = [1., 0.5, 1., 1., 1., 1., 1.]
        >>> cov_nb = H2ONaiveBayesEstimator(class_sampling_factors=sample_factors,
        ...                                 seed=1234)
        >>> predictors = covtype.columns[0:54]
        >>> response = 'C55'
        >>> cov_nb.train(x=predictors, y=response, training_frame=covtype)
        >>> cov_nb.logloss()
        """
        return self._parms.get("class_sampling_factors")

    @class_sampling_factors.setter
    def class_sampling_factors(self, class_sampling_factors):
        assert_is_type(class_sampling_factors, None, [float])
        self._parms["class_sampling_factors"] = class_sampling_factors

    @property
    def max_after_balance_size(self):
        """
        Maximum relative size of the training data after balancing class counts (can be less than 1.0). Requires
        balance_classes.

        Type: ``float``, defaults to ``5.0``.

        :examples:

        >>> covtype = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/covtype/covtype.20k.data")
        >>> covtype[54] = covtype[54].asfactor()
        >>> predictors = covtype.columns[0:54]
        >>> response = 'C55'
        >>> train, valid = covtype.split_frame(ratios=[.8], seed=1234)
        >>> max = .85
        >>> cov_nb = H2ONaiveBayesEstimator(max_after_balance_size=max,
        ...                                 seed=1234) 
        >>> cov_nb.train(x=predictors,
        ...              y=response,
        ...              training_frame=train,
        ...              validation_frame=valid)
        >>> cars_nb.logloss()
        """
        return self._parms.get("max_after_balance_size")

    @max_after_balance_size.setter
    def max_after_balance_size(self, max_after_balance_size):
        assert_is_type(max_after_balance_size, None, float)
        self._parms["max_after_balance_size"] = max_after_balance_size

    @property
    def max_confusion_matrix_size(self):
        """
        [Deprecated] Maximum size (# classes) for confusion matrices to be printed in the Logs

        Type: ``int``, defaults to ``20``.
        """
        return self._parms.get("max_confusion_matrix_size")

    @max_confusion_matrix_size.setter
    def max_confusion_matrix_size(self, max_confusion_matrix_size):
        assert_is_type(max_confusion_matrix_size, None, int)
        self._parms["max_confusion_matrix_size"] = max_confusion_matrix_size

    @property
    def laplace(self):
        """
        Laplace smoothing parameter

        Type: ``float``, defaults to ``0.0``.

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate.csv.zip")
        >>> prostate['CAPSULE'] = prostate['CAPSULE'].asfactor()
        >>> prostate['RACE'] = prostate['RACE'].asfactor()
        >>> prostate['DCAPS'] = prostate['DCAPS'].asfactor()
        >>> prostate['DPROS'] = prostate['DPROS'].asfactor()
        >>> prostate_nb = H2ONaiveBayesEstimator(laplace=1)
        >>> prostate_nb.train(x=list(range(3,9)),
        ...                   y=response_col,
        ...                   training_frame=prostate)
        >>> prostate_nb.mse()
        """
        return self._parms.get("laplace")

    @laplace.setter
    def laplace(self, laplace):
        assert_is_type(laplace, None, numeric)
        self._parms["laplace"] = laplace

    @property
    def min_sdev(self):
        """
        Min. standard deviation to use for observations with not enough data

        Type: ``float``, defaults to ``0.001``.

        :examples:

        >>> import random
        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> problem = random.sample(["binomial","multinomial"],1)
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> if problem == "binomial":
        ...     response_col = "economy_20mpg"
        ... else:
        ...     response_col = "cylinders"
        >>> cars[response_col] = cars[response_col].asfactor()
        >>> cars_nb = H2ONaiveBayesEstimator(min_sdev=0.1,
        ...                                  eps_sdev=0.5,
        ...                                  seed=1234)
        >>> cars_nb.train(x=predictors,
        ...               y=response_col,
        ...               training_frame=cars)
        >>> cars_nb.show()
        """
        return self._parms.get("min_sdev")

    @min_sdev.setter
    def min_sdev(self, min_sdev):
        assert_is_type(min_sdev, None, numeric)
        self._parms["min_sdev"] = min_sdev

    @property
    def eps_sdev(self):
        """
        Cutoff below which standard deviation is replaced with min_sdev

        Type: ``float``, defaults to ``0.0``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> problem = random.sample(["binomial","multinomial"],1)
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> if problem == "binomial":
        ...     response_col = "economy_20mpg"
        ... else:
        ...     response_col = "cylinders"
        >>> cars[response_col] = cars[response_col].asfactor()
        >>> cars_nb = H2ONaiveBayesEstimator(min_sdev=0.1,
        ...                                  eps_sdev=0.5,
        ...                                  seed=1234)
        >>> cars_nb.train(x=predictors, y=response_col, training_frame=cars)
        >>> cars_nb.mse()
        """
        return self._parms.get("eps_sdev")

    @eps_sdev.setter
    def eps_sdev(self, eps_sdev):
        assert_is_type(eps_sdev, None, numeric)
        self._parms["eps_sdev"] = eps_sdev

    @property
    def min_prob(self):
        """
        Min. probability to use for observations with not enough data

        Type: ``float``, defaults to ``0.001``.

        :examples:

        >>> import random
        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> problem = random.sample(["binomial","multinomial"],1)
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> if problem == "binomial":
        ...     response_col = "economy_20mpg"
        ... else:
        ...     response_col = "cylinders"
        >>> cars[response_col] = cars[response_col].asfactor()
        >>> cars_nb = H2ONaiveBayesEstimator(min_prob=0.1,
        ...                                  eps_prob=0.5,
        ...                                  seed=1234)
        >>> cars_nb.train(x=predictors,
        ...               y=response_col,
        ...               training_frame=cars)
        >>> cars_nb.show()
        """
        return self._parms.get("min_prob")

    @min_prob.setter
    def min_prob(self, min_prob):
        assert_is_type(min_prob, None, numeric)
        self._parms["min_prob"] = min_prob

    @property
    def eps_prob(self):
        """
        Cutoff below which probability is replaced with min_prob

        Type: ``float``, defaults to ``0.0``.

        :examples:

        >>> import random
        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> problem = random.sample(["binomial","multinomial"],1)
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> if problem == "binomial":
        ...     response_col = "economy_20mpg"
        ... else:
        ...     response_col = "cylinders"
        >>> cars[response_col] = cars[response_col].asfactor()
        >>> cars_nb = H2ONaiveBayesEstimator(min_prob=0.1,
        ...                                  eps_prob=0.5,
        ...                                  seed=1234)
        >>> cars_nb.train(x=predictors, y=response_col, training_frame=cars)
        >>> cars_nb.mse()
        """
        return self._parms.get("eps_prob")

    @eps_prob.setter
    def eps_prob(self, eps_prob):
        assert_is_type(eps_prob, None, numeric)
        self._parms["eps_prob"] = eps_prob

    @property
    def compute_metrics(self):
        """
        Compute metrics on training data

        Type: ``bool``, defaults to ``True``.

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate.csv.zip")
        >>> prostate['CAPSULE'] = prostate['CAPSULE'].asfactor()
        >>> prostate['RACE'] = prostate['RACE'].asfactor()
        >>> prostate['DCAPS'] = prostate['DCAPS'].asfactor()
        >>> prostate['DPROS'] = prostate['DPROS'].asfactor()
        >>> response_col = 'CAPSULE'
        >>> prostate_nb = H2ONaiveBayesEstimator(laplace=0,
        ...                                      compute_metrics=False)
        >>> prostate_nb.train(x=list(range(3,9)),
        ...                   y=response_col,
        ...                   training_frame=prostate)
        >>> prostate_nb.show()
        """
        return self._parms.get("compute_metrics")

    @compute_metrics.setter
    def compute_metrics(self, compute_metrics):
        assert_is_type(compute_metrics, None, bool)
        self._parms["compute_metrics"] = compute_metrics

    @property
    def max_runtime_secs(self):
        """
        Maximum allowed runtime in seconds for model training. Use 0 to disable.

        Type: ``float``, defaults to ``0.0``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> cars["economy_20mpg"] = cars["economy_20mpg"].asfactor()
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> response = "economy_20mpg"
        >>> train, valid = cars.split_frame(ratios=[.8], seed=1234)
        >>> cars_nb = H2ONaiveBayesEstimator(max_runtime_secs=10,
        ...                                  seed=1234) 
        >>> cars_nb.train(x=predictors,
        ...               y=response,
        ...               training_frame=train,
        ...               validation_frame=valid)
        >>> cars_nb.auc()
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
        >>> airlines = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip", destination_frame="air.hex")
        >>> predictors = ["DayofMonth", "DayOfWeek"]
        >>> response = "IsDepDelayed"
        >>> checkpoints_dir = tempfile.mkdtemp()
        >>> air_nb = H2ONaiveBayesEstimator(export_checkpoints_dir=checkpoints_dir)
        >>> air_nb.train(x=predictors, y=response, training_frame=airlines)
        >>> len(listdir(checkpoints_dir))
        """
        return self._parms.get("export_checkpoints_dir")

    @export_checkpoints_dir.setter
    def export_checkpoints_dir(self, export_checkpoints_dir):
        assert_is_type(export_checkpoints_dir, None, str)
        self._parms["export_checkpoints_dir"] = export_checkpoints_dir

    @property
    def gainslift_bins(self):
        """
        Gains/Lift table number of bins. 0 means disabled.. Default value -1 means automatic binning.

        Type: ``int``, defaults to ``-1``.

        :examples:

        >>> airlines= h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/testng/airlines_train.csv")
        >>> model = H2ONaiveBayesEstimator(gainslift_bins=20)
        >>> model.train(x=["Origin", "Distance"],
        ...             y="IsDepDelayed",
        ...             training_frame=airlines)
        >>> model.gains_lift()
        """
        return self._parms.get("gainslift_bins")

    @gainslift_bins.setter
    def gainslift_bins(self, gainslift_bins):
        assert_is_type(gainslift_bins, None, int)
        self._parms["gainslift_bins"] = gainslift_bins

    @property
    def auc_type(self):
        """
        Set default multinomial AUC type.

        Type: ``Literal["auto", "none", "macro_ovr", "weighted_ovr", "macro_ovo", "weighted_ovo"]``, defaults to
        ``"auto"``.
        """
        return self._parms.get("auc_type")

    @auc_type.setter
    def auc_type(self, auc_type):
        assert_is_type(auc_type, None, Enum("auto", "none", "macro_ovr", "weighted_ovr", "macro_ovo", "weighted_ovo"))
        self._parms["auc_type"] = auc_type

