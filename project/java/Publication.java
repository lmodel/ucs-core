package None;

import java.util.List;
import lombok.*;






/**
  Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Csolink category subclasses.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Publication extends InformationContentEntity {

  private List<String> authors;
  private List<String> pages;
  private String summary;
  private List<String> keywords;
  private List<String> lcshTerms;

}