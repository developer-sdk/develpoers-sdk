package sdk.functional;

import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;

/**
 * 리스트를 이용한 이터레이션
 * 
 * @author whitebeard-k
 *
 */
public class FunctionalExample02 {

	public static final List<String> friends = Arrays.asList("Brian", "Nate", "Neal", "Raju", "Sara", "Scott");

	// 명령형 처리
	public static void for_Imperative(List<String> list) {
		// 인덱스를 이용한 직접 접근은 문제가 발생할 여지가 있다.
		// 특정 인덱스에 대한 직접 접근일 때 유리
		for (int i = 0; i < friends.size(); i++) {
			System.out.println(friends.get(i));
		}

		// 좀 더 향상된 방법
		// 향상된 for 문을 이용한 처리
		for (String name : friends) {
			System.out.println(name);
		}
	}

	// 서술형 처리
	public static void for_declarative(List<String> list) {
		// forEach를 Consumer 인터페이스를 이용하여 처리
		// 내부 이터레이터를 이용하여 처리한다.
		// 각 엘리먼트를 어떻게 이터레이션하는지에 대해서는 생각할 필요 없이 처리가 가능하다.
		// 하지만 코드가 장황해짐
		friends.forEach(new Consumer<String>() {
			public void accept(final String name) {
				System.out.println(name);
			}
		});

		// 람다 표현식을 이용하여 간결하게 표현
		// 각 엘리먼트를 사용해서 하고자 하는 목적에 초점을 맞출수 있다.
		// 람다 표현식을 간결하게 사용하여 더 간단하게 사용할 수 있다. 다음은 모두 같은 결과를 출력한다. 
		friends.forEach((final String name) -> System.out.println(name));
		friends.forEach((name) -> System.out.println(name));
		friends.forEach(name -> System.out.println(name));
		friends.forEach(System.out::println);
	}

	public static void main(final String[] args) {

		for_Imperative(friends);
		for_declarative(friends);
	}
}