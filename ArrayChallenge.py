'''
Array Challenge
Have the function ArrayChallenge(strArr) read the array of strings stored in strArr, which will contain 2 elements: the first element will be a sequence of characters, and the second element will be a long string of comma-separated words, in alphabetical order, that represents a dictionary of some arbitrary length. For example: strArr can be: ["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]. Your goal is to determine if the first element in the input can be split into two words, where both words exist in the dictionary that is provided in the second input. In this example, the first element can be split into two words: hello and cat because both of those words are in the dictionary.

Your program should return the two words that exist in the dictionary separated by a comma. So for the example above, your program should return hello,cat. There will only be one correct way to split the first element of characters into two words. If there is no way to split string into two words that exist in the dictionary, return the string not possible. The first element itself will never exist in the dictionary as a real word.
Once your function is working, take the final output string and concatenate it with your ChallengeToken, and then replace every fourth character with an underscore.

Your ChallengeToken: wglefn8vq0d
Examples
Input: ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]
Output: base,ball
Final Output: bas_,ba_lwg_efn_vq0_
Input: ["abcgefd", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]
Output: abcg,efd
Final Output: abc_,ef_wgl_fn8_q0d
'''

def ArrayChallenge(strArr):

  #str
  first = strArr[0]
  #strArr
  second = strArr[1].split(",")

  for i in range(len(first) - 1):
    left, right = first[:i + 1], first[i + 1:]
    if left in second and right in second:
      out = f"{left},{right}wglefn8vq0d"
      k = "_"
      n = 4
      fout = ""
      for idx, ele in enumerate(out):
        if (idx + 1) % 4 == 0:
          fout = fout + k
        else:
          fout = fout + ele
      return fout


  out = "not possiblewglefn8vq0d"
  k = "_"
  n = 4
  fout = ""
  for idx, ele in enumerate(out):
    if (idx + 1) % 4 == 0:
      fout = fout + k
    else:
      fout = fout + ele
  return fout

# keep this function call here
print(ArrayChallenge(input()))
