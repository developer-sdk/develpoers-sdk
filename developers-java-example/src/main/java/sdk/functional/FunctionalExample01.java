package sdk.functional;

import java.util.List;
import java.util.Arrays;

/**
 * 명령형 스타일과 서술형 스타일 코드 
 * 
 * @author whitebeard-k
 *
 */
public class FunctionalExample01 {

	// 명령형 스타일 코드
	public static void findC_Imperative(final List<String> cities) {
		boolean found = false;
		for (String city : cities) {
			if (city.equals("C")) {
				found = true;
				break;
			}
		}

		System.out.println("Found C?:" + found);
	}

	// 서술형 스타일 코드
	public static void findC_Declarative(final List<String> cities) {
		System.out.println("Found C?:" + cities.contains("C"));
	}

	public static void main(final String[] args) {
		List<String> strs = Arrays.asList("A", "B", "C", "D", "E");

		findC_Imperative(strs);
		findC_Declarative(strs);
	}
}