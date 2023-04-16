package None;

import java.util.List;
import lombok.*;






/**
  Root Universal Model class for all things and informational relationships, real or imagined.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class Entity  {

  private String id;
  private String iri;
  private List<String> category;
  private String type;
  private String name;
  private String description;
  private List<Attribute> hasAttribute;

}