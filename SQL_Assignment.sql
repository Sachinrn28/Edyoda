create database assignment;
use assignment;
create table salespeople (snum int,sname varchar(50),city varchar(50),comm int);
insert into salespeople(snum,sname,city,comm) values(1001,"Peel","london",12),(1002,"Serres","Sanjose",13),(1004,"Motika","london",11),(1007,"Rifkin","Barcelona",15),(1003," Axelrod","Newyork",10);
select*from salespeople;
create table customer (cnum int,cname varchar(50),city varchar(50),snum int);
insert into customer(cnum,cname,city,snum) values(2001,"Hoffman","London",1001),(2002," Giovanni","Rome",1003),(2003,"Liu","Sanjose",1002),(2004,"Grass","Berlin",1002),(2006,"Clemens","London ",1001),(2008,'Cisneros','Sanjose',1007),(2007,'Pereira','Rome',1004);
select*from customer;
create table orders(Onum int,Amt int,Odate int,Cnum int,Snum int);
insert into orders(Onum,Amt,Odate,Cnum,Snum) values(3001,18.69,3-10-1990,2008,1007),(3003,767.19,3-10-1990,2001,1001),(3002,1900.10,3-10-1990,2007,1004),(3005,5160.45,3-10-1990,2003,1002),(3006,1098.16,3-10-1990,2008,1007),(3009,1713.23,4-10-1990,2002,1003),(3007,75.75,4-10-1990,2004,1002),(3008,4273.00,5-10-1990,2006,1001),(3010,1309.95,6-10-1990,2004,1002),(3011 ,9891.88,6-10-1990,2006,1001);
select*from orders;
select*from salespeople;
--  Count the number of Salesperson whose name begin with ‘a’/’A’.
SELECT COUNT(*) FROM salespeople where Sname like "%A" or "%a";
-- Display all the Salesperson whose all orders worth is more than Rs. 2000.
SELECT Snum, Sname, City, Comm
FROM SalesPeople 
WHERE Snum IN (
    SELECT Snum
    FROM Orders 
    GROUP BY Snum
    HAVING SUM(Amt) > 2000
);
-- QCount the number of Salesperson belonging to Newyork.
-- Solution:
SELECT COUNT(*)
FROM SalesPeople
WHERE City = 'Newyork';

-- Display the number of Salespeople belonging to London and belonging to Paris.
-- Solution:
SELECT City, COUNT(*) as NumberOfSalespeople
FROM SalesPeople
WHERE City IN ('London', 'Paris')
GROUP BY City;

-- Display the number of orders taken by each Salesperson and their date of orders.
-- Solution:
SELECT S.Snum, S.Sname, O.Odate, COUNT(*) AS NumberOfOrders
FROM SalesPeople as S
JOIN Orders as O ON S.Snum = O.Snum
GROUP BY S.Snum, S.Sname, O.Odate
ORDER BY S.Snum, O.Odate;
