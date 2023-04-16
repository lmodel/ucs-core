package None;

import java.util.List;
import lombok.*;






/**
  A mixin that can be used on any entity that can be taxonomically classified. This includes individual entities, their products, and other operational entities and processes.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ThingWithTaxon  {

  private List<NamedThing> inTaxon;

}