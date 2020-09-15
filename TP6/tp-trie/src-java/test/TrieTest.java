import trie.Trie ;
import static org.junit.Assert.*;

import org.junit.Test;

public class TrieTest {

	@Test
	public void addTest(){
		Trie t = new Trie();
		t.add("banane");
		assertTrue(t.contains("banane"));
		t.add("citronnier");
		assertTrue(t.contains("citronnier"));
		t.add("citron");
		assertTrue(t.contains("citron"));
		t.add("pomme");
		assertTrue(t.contains("pomme"));
		t.add("poire");
		assertTrue(t.contains("poire"));
		t.add("ci");
		assertTrue(t.contains("ci"));
		t.add("anticonstitutionnellement");
		assertTrue(t.contains("anticonstitutionnellement"));
		t.add("zeppelins");
		assertTrue(t.contains("zeppelins"));
		assertFalse(t.contains("tulipe"));
	}

	// ---Pour permettre l'execution des tests ----------------------
	public static junit.framework.Test suite() {
		return new junit.framework.JUnit4TestAdapter(TrieTest.class);
	}

}
