# 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164671
# 작성자: 손삼주
# 작성일: 2026. 02. 26. 10:30:41

-- 파일경로: /home/grep/src/BOARD_ID/FILE_IDFILE_NAME.FILE_EXT
SELECT CONCAT('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID = (SELECT BOARD_ID
FROM USED_GOODS_BOARD
WHERE VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
)
ORDER BY FILE_ID DESC
