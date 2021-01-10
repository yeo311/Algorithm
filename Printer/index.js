// https://programmers.co.kr/learn/courses/30/lessons/42587
// 프로그래머스 스택/큐 "프린터" 문제

function solution(priorities, location) {
  var answer = 0;
  
  // priorities를 2차원배열로 변경하여 내가 요청한 문서에 true flag를 마킹함.
  priorities = priorities.map((item, i) => {
      if (i === location) {
          return [item, true];
      } else {
          return [item, false];
      }
  });
  
  while (priorities.length > 0) {
      let j = priorities.shift();
      let exist = false;
      
      // 중요도가 더 높은 문서가 있는 지 확인
      for (let i = 0; i < priorities.length; i++) {
          if (priorities[i][0] > j[0]) {
              exist = true;
              break;
          }
      }
      if (!exist) {
          // 중요도가 더 높은 문서가 없으면 현재 문서를 출력(answer++) 하고,
          // 출력한 문서가 내가 요청한 문서면 반복문 종료.
          answer++;
          if (j[1] === true) {
              break;
          }
      } else {
          // 중요도가 더 높은 문서가 있으면 현재 문서를 대기목록 뒤로 보냄
          priorities.push(j)
      }
  }
  
  return answer;
}