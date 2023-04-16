package None;

import java.util.List;
import lombok.*;






/**
  A value of an attribute that is quantitative and measurable, available as a combination of a unit and a numeric value
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class QuantityValue extends Annotation {

  private String hasUnit;
  private Double hasNumericValue;

}