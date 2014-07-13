select summ from (
    select a.row_num, b.col_num, SUM(a.value*b.value) as summ
    from a, b where a.col_num = b.row_num
    group by a.row_num, b.col_num
    )
where col_num=3 and row_num=2;
