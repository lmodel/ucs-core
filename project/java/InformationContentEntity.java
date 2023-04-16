package None;

import java.util.List;
import lombok.*;






/**
  A piece of information that typically describes some topic of discourse or is used as support.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class InformationContentEntity extends NamedThing {

  private String license;
  private String rights;
  private String format;
  private String creationDate;

}