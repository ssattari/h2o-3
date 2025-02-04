package water.automl.api.schemas3;

import ai.h2o.automl.preprocessing.PipelineStepDefinition;
import water.api.API;
import water.api.EnumValuesProvider;
import water.api.Schema;

import static ai.h2o.automl.preprocessing.PipelineStepDefinition.*;

public final class PipelineStepDefinitionV99 extends Schema<PipelineStepDefinition, PipelineStepDefinitionV99> {

  public static final class TypeProvider extends EnumValuesProvider<Type> {
    public TypeProvider() {
      super(Type.class);
    }
  }

  @API(help="A type representing the preprocessing step to be executed.", valuesProvider=TypeProvider.class, direction=API.Direction.INOUT)
  public Type type;

}

