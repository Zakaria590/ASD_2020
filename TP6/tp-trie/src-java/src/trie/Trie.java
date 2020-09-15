package trie ;
import java.util.HashMap;
/**
 * Class Trie
 *
 * @author OUAICHOUCHE
 * @version 1.0
 */ 

public class Trie {

   private HashMap<Character, Trie> arbre;

   /**
    * create a empty trie
    */
   public Trie () {
      this.arbre = new HashMap<Character, Trie>();
   }

   /**
    * add a word in the Trie
    * @param word the word to be added
    */
   public void add (String word) {
     if(word.length()>0){
      Trie trie = new Trie();
      trie.add(word.substring(1));
      this.arbre.put(word.charAt(0), trie);
    }
   }

   /**
    * verify if a word is in the trie
    * @param word the word to be verify
    * @return true if the word is in trie, false otherwise
    */
   public boolean contains (String word) {
     if(word.length() == 0) return true;
     Trie trie = this.arbre.get(word.charAt(0));
     if(trie == null) return false;
     else return (trie != null) || trie.contains(word.substring(1));
   }


  /**
  * print the trie
  */
   public void print () {
     for (Character i : this.arbre.keySet()) {
       System.out.println(i);
      }
   }
}
