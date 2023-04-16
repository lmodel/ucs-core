package None;

import java.util.List;
import lombok.*;






/**
  An entity that intends to perform some functions, interacting with other systems. Relative to a given system, the entities with which it interacts, are considered its environment. A system is structurally composed of a set of components bound together.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class System extends NamedThing {

  private List<NamedThing> inTaxon;

}