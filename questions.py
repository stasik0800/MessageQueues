

q = {'q1': """select 
                     t.name as Song,
                     ar.name as Compositor ,
                     ge.name as Genres
             from tracks t
            join genres ge on t.genreid = ge.genreid
            join albums al on al.albumid = t.albumid
            join artists ar on ar.artistid =  al.artistid;""",

     'q2': """select 
			    c.FirstName as FirstName,
			    c.LastName  as LastName,
			    c.Phone  as Phone,
			    c.email as email, 
			    (ifnull(c.country,'') || ' ' || ifnull(c.state,'')  || ' ' ||  ifnull(c.city,'')  ||  ' ' ||  ifnull(c.address,'') ) as full_address ,
			    sum(quantity) as quantity_orders
             from invoice_items it
            join invoices i  on it .invoiceid = i.invoiceid
            join customers c on c.customerid = i.customerid
             group by 	c.FirstName,
                        c.LastName,
                        c.Phone ,
                        c.email, 
			            (ifnull(c.country,'') || ' ' || ifnull(c.state,'')  || ' ' ||  ifnull(c.city,'')  ||  ' ' ||  ifnull(c.address,'') )
            order by 6;""",

     'q3': """ select  
                    country,
                    domain,
                    count(*) as number_of_domain_in_country 
                    from (
                            select country, replace(substr(email, instr(email, '@') + 1), ltrim(substr(email, instr(email, '@') + 1), replace(substr(email, instr(email, '@') + 1), '.', '')), '')  as domain
                            from customers
                          union all 
                            select country,replace(substr(email, instr(email, '@') + 1), ltrim(substr(email, instr(email, '@') + 1), replace(substr(email, instr(email, '@') + 1), '.', '')), '')  as domain
                            from employees
                          ) 
                    group by country,domain
                    order by 1,3 ;""",

    'q4': """  select 
                      sum(it.quantity) as amount_tracks_sold ,
                      billingcountry
                    from invoices i
                    join invoice_items it on it.invoiceid =  i.invoiceid
                    group by billingcountry;""",

    'q5': """ select            
                        title as cd_albume,
                        billingcountry as billing_country,
                        max(amount_of_sales) as highiest_amount_of_sales,
                        amount_of_incomes
                    from (
                                select  
                                    billingcountry,
                                    sum(it.quantity) as amount_of_sales,
                                    sum(it.unitPrice) as amount_of_incomes ,
                                    a.title
                                 from invoices i
                                join invoice_items it on it.invoiceid =  i.invoiceid
                                join tracks t on t.trackid=it.trackid
                                join albums a on a.albumid = t.albumid
                                group by billingcountry,a.title
                    ) tb 
                    group by billingcountry
                    order by 3 desc;""",

    'q6': """ select   a.title,
		               sum(it.quantity) as total_sales
              from (			
                      select invoiceid 
                      from invoices 
                      where date(invoicedate)>='2011-01-01'  and billingCountry='USA'
                    ) i
              join invoice_items it on it.invoiceid =  i.invoiceid
              join tracks t on t.trackid=it.trackid
              join albums a on a.albumid = t.albumid
              group by a.title
              order by 2 desc
              limit 1;""",

    'q7': """       select * from customers
                     where customerid in (
                                         select customerid
                                         from (
                                             select c.customerid,
                                            case  when FirstName is null then 1 else 0  end FirstName ,
                                            case  when LastName is null then 1 else 0  end LastName,
                                            case  when Company is null then 1 else 0  end Company,
                                            case  when Address is null then 1 else 0  end Address,
                                            case  when City is null then 1 else 0  end City,
                                            case  when Country is null then 1 else 0  end Country,
                                            case  when PostalCode is null then 1 else 0  end PostalCode,
                                            case  when Fax is null then 1 else 0  end Fax,
                                            case  when Phone is null then 1 else 0  end Phone,
                                            case  when Email is null then 1 else 0  end Email
                                             from customers c
                                        )where (FirstName+LastName+Company+Address+City+Country+PostalCode+Fax+Phone+Email) >=2
                    );
    """}
