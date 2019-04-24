package sdk.stream;

import java.util.List;
import java.util.Arrays;

public class StreamExample {

	// 명령형 스타일 코드
	public static void findChicagoImperative(final List<String> cities) {
		boolean found = false;
		for (String city : cities) {
			if (city.equals("Chicago")) {
				found = true;
				break;
			}
		}

		System.out.println("Found chicago?:" + found);
	}

	// 서술형 스타일 코드
	public static void findChicagoDeclarative(final List<String> cities) {
		System.out.println("Found chicago?:" + cities.contains("Chicago"));
	}

	public static void main(final String[] args) {
		List<String> cities = Arrays.asList("Albany", "Boulder", "Chicago", "Denver", "Eugene");

		findChicagoImperative(cities);
		findChicagoDeclarative(cities);
	}
}