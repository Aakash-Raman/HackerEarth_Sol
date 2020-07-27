/* IMPORTANT: Multiple classes and nested static classes are supported */

/*
 * uncomment this if you want to read input.
//imports for BufferedReader
import java.io.BufferedReader;
import java.io.InputStreamReader;

//import for Scanner and other utility classes
import java.util.*;
*/

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

import java.util.Scanner; 
import java.util.Stack;


public class Brackets { 

public static void main(String[] args) { 

 Scanner sc = new Scanner(System.in); 
 int t = sc.nextInt(); 
 sc.nextLine(); 
 while (t-- != 0) { 
  String s = sc.nextLine(); 
  Stack<Character> stack = new Stack<Character>(); 
  boolean isBalanced = true; 

  for (int i = 0; i < s.length(); i++) { 

   char ch = s.charAt(i); 
   if (ch == '(' || ch == '{' || ch == '[') { 
    stack.push(ch); 
    continue; 
   } 

   if (stack.isEmpty()) { 
    isBalanced = false; 
    break; 
   } 

   else if (ch == ')') { 
    if (stack.peek() == '(') { 
     stack.pop(); 
    } else { 
     isBalanced = false; 
     break; 
    } 
   } else if (ch == '}') { 
    if (stack.peek() == '{') { 
     stack.pop(); 
    } else { 
     isBalanced = false; 
     break; 
    } 
   } else if (ch == ']') { 
    if (stack.peek() == '[') { 
     stack.pop(); 
    } else { 
     isBalanced = false; 
     break; 
    } 
   } 

  } 
  if (!stack.isEmpty()) { 
   isBalanced = false; 

  } 
  if (isBalanced) { 
   System.out.println("YES"); 
  } else { 
   System.out.println("NO"); 
  } 
 } 

} 

} 
