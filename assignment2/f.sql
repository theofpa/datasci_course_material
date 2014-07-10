--(f) two words: Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'.
select count(one.docid) from frequency one, frequency two where one.docid=two.docid and one.term='transactions' and two.term='world';
