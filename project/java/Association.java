package None;

import java.util.List;
import lombok.*;






/**
  A typed association between two entities, supported by evidence
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Association extends Entity {

  private NamedThing subject;
  private String predicate;
  private NamedThing object;
  private boolean negated;
  private List<OntologyClass> qualifiers;
  private List<Publication> publications;
  private List<EvidenceType> hasEvidence;

}