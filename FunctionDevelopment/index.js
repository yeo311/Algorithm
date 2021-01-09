// https://programmers.co.kr/learn/courses/30/parts/12081
// 프로그래머스 스택/큐 기능개발 문제

function solution(progresses, speeds) {
  var answer = [];
  let spendDays = 0;
  let count = 0;
  
  for (let i = 0; i < progresses.length; i++) {
      // 작업에 소요되는데 필요한 기간을 구함
      let needDays = Math.floor((100 - progresses[i]) / speeds[i]);
      if ((100 - progresses[i]) % speeds[i] > 0) {
          needDays++;
      }
      
      // 필요한 기간(needDays)이 이미 소요된 기간(spendDays)보다 클 경우,
      // 이전까지 완료된 기능들(count)을 answer에 push해주고 count는 초기화.
      if (spendDays < needDays) {
          spendDays = needDays;
          if (count > 0) {
              answer.push(count);    
              count = 0;
          }
      }
      
      count++;
      
      // 마지막에는 나머지 기능들 count를 push.
      if (i === progresses.length - 1) {
          answer.push(count);
      }
  }
  
  return answer;
}