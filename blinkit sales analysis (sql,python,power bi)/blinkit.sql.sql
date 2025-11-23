SELECT * FROM blinkit.b;
select count(*) from b;
SELECT CAST(SUM(Sales)/1000000 AS DECIMAL(10,2)) AS total_sales_million 
FROM b 
group by `Item Fat Content`;

select cast(avg(sales) as decimal(10,2)) as average_sales from b;
select cast(avg(Rating) as decimal(10,2)) as avg_rating from b;

#total sales by fat content;
SELECT `Item Fat Content`,
concat(cast(SUM(Sales)/1000 AS DECIMAL(10,2)), 'k')AS total_sales_thousand,
count(*),
cast(avg(Rating) as decimal(10,2)) as avg_rating ,
cast(avg(sales) as decimal(10,2)) as average_sales
FROM b 
where `Outlet Establishment Year`= 2022
group by `Item Fat Content` order by total_sales_thousand desc;

#total sales by item type ;
  SELECT `Item Type`,
concat(cast(SUM(Sales)/1000 AS DECIMAL(10,2)), 'k')AS total_sales_thousand,
count(*),
cast(avg(Rating) as decimal(10,2)) as avg_rating ,
cast(avg(sales) as decimal(10,2)) as average_sales
FROM b 
group by `Item Type` order by total_sales_thousand desc;

select `Item type`,count(`Item type`) from b
group by `Item type`;

# fat content by outlet for total sales ;
select `Item Fat Content`,`Outlet Location Type`,concat(cast(SUM(Sales)/1000 AS DECIMAL(10,2)), 'k')AS total_sales_thousand,
count(*),
cast(avg(Rating) as decimal(10,2)) as avg_rating ,
cast(avg(sales) as decimal(10,2)) as average_sales
from b
group by `Item Fat Content`, `Outlet Location Type`
order by total_sales_thousand desc;

# fat content by outlet for total sales  original and professional;

select IFNULL(`Outlet Location Type`, 'TOTAL') AS `Outlet Location Type`,
  round(sum(case when `Item Fat Content`= 'Low Fat' then sales else 0 end),2) as low_fat,
  round(sum(case when `Item Fat Content`= 'Regular' then sales else 0 end),2) as regular,
round(sum(case when `Item Fat Content`= 'LF' then sales else 0 end),2) as lf,
round(sum(case when `Item Fat Content`= 'reg' then sales else 0 end),2) as reg
from b
group by `Outlet Location Type` with rollup
order by `Outlet Location Type`;

#total sales by outlet establishment year ;
  SELECT `Outlet Establishment Year`,
concat(cast(SUM(Sales)/1000 AS DECIMAL(10,2)), 'k')AS total_sales_thousand,
count(*) from b
group by `Outlet Establishment Year`
order by `Outlet Establishment Year` asc;

select ifnull(count(`Outlet Establishment Year`),'total') as `Outlet Establishment Year`,`Outlet Establishment Year` from b
group by `Outlet Establishment Year` with rollup;

# percentage of sales by outlet size;
select `Outlet Size`,
cast(sum(`sales`) as decimal(10,2)) as total_sales,
cast(sum(`sales`)*100 / (select sum(`sales`) from b) as decimal(10,2)) as percentrage_sales
from b
group by `Outlet Size`
order by percentrage_sales desc;


select cast(sum(`sales`)*100 / (select sum(`sales`) from b) as decimal(10,2)) as percentrage_sales from b;

#sales by outlet location;
select sum(`sales`) as total_sales, `Outlet Location Type`
from b
group by `Outlet Location Type`
order by total_sales;

#all the metrics by outlet type;

select `Outlet Type`,
concat(cast(SUM(Sales)/1000 AS DECIMAL(10,2)), 'k')AS total_sales_thousand,
count(*),
cast(avg(Rating) as decimal(10,2)) as avg_rating ,
cast(avg(sales) as decimal(10,2)) as average_sales,
cast(sum(`sales`)*100 / (select sum(`sales`) from b) as decimal(10,2)) as percentrage_sales
from b
group by `Outlet Type`;