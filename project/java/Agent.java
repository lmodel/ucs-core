package None;

import java.util.List;
import lombok.*;






/**
  person, group, organization or project that provides a piece of information (i.e. a knowledge association)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Agent extends AdministrativeEntity {

  private List<String> affiliation;
  private String address;

}