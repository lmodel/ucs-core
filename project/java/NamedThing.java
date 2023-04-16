package None;

import java.util.List;
import lombok.*;






/**
  a databased entity or concept/class
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NamedThing extends Entity {

  private List<String> providedBy;
  private List<String> xref;

}