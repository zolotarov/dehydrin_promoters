# Dehydrins project

## 20141106, Thursday, November 6, 2014

### Kn Seeder results

```
>matrix 2.1449e-05
12 0 8 19
10 17 11 1
14 0 20 5
1 38 0 0
0 38 1 0
9 9 21 0
31 8 0 0
0 39 0 0
39 0 0 0
8 7 2 22
9 17 7 6
6 6 16 11
```

### SKn Seeder results

```
>matrix 2.19758e-44
26 31 29 35
32 39 23 27
29 57 28 7
111 3 7 0
1 118 1 1
0 118 0 3
1 2 117 1
105 13 2 1
0 118 3 0
38 47 23 13
15 13 2 91
6 45 28 42
>matrix 9.40136e-20
53 64 1 3
10 100 4 7
102 1 12 6
2 112 0 7
15 3 95 8
1 31 1 88
2 0 116 3
0 12 29 80
8 111 2 0
51 17 31 22
27 32 22 40
4 56 45 16
>matrix 9.99405e-10
24 34 48 15
8 64 47 2
15 83 19 4
75 5 37 4
115 5 1 0
10 97 4 10
15 0 105 1
0 110 3 8
36 5 77 3
35 18 60 8
59 28 11 23
18 5 71 27
>matrix 2.70496e-08
52 7 34 27
19 1 49 52
26 11 52 32
1 1 119 0
17 0 2 102
0 78 41 2
1 0 119 1
1 0 118 2
6 40 2 73
12 45 38 26
13 46 19 43
35 25 27 34
>matrix 1.70584e-06
19 8 68 26
76 21 12 12
38 6 75 2
103 0 7 11
2 0 114 5
56 22 29 14
1 0 115 5
60 1 2 58
4 1 107 9
34 1 83 3
61 8 39 13
26 1 87 7
>matrix 3.41169e-06
17 47 15 42
11 83 24 3
10 87 24 0
119 0 0 2
11 110 0 0
8 11 94 8
6 2 0 113
17 4 30 70
54 28 38 1
9 70 1 41
45 40 18 18
18 57 24 22
>matrix 0.000154216
30 35 50 6
48 16 41 16
43 34 13 31
0 120 1 0
51 3 52 15
3 115 1 2
8 7 102 4
3 0 4 114
73 35 12 1
53 23 22 23
21 22 46 32
26 68 4 23
>matrix 0.00612833
83 7 2 29
56 19 24 22
96 0 11 14
103 4 14 0
2 1 4 114
115 0 6 0
121 0 0 0
4 47 1 69
3 7 110 1
14 34 33 39
52 22 35 11
56 10 37 17
```



## 20141105 Wednesday, November 5, 2014

Added new column to the database, "use" indicating whether the gene is used or not.
Checking the promoter fasta files in the `sequences/promoters` dir.

---
**Kn**: 41 in the database `

```sql
SELECT COUNT(gene) FROM genes WHERE subgroup_category="Kn" AND latest="Yes";
```

38 in the Kn_prom.fas file

`MA_4978040g0010` absent because it has no promoter, added use="No".  
`MDP0000196703`  absent because it has no promoter, added use="No".  
`Gorai.007G257100` absent for unknown reason.  

---
**KS**: 47 in DB and file

---
**SKn**
118 in file 122 in DB.

```sql
SELECT gene FROM genes WHERE subgroup_category="SKn" AND latest="Yes" ORDER BY gene COLLATE NOCASE ASC;
```
COLLATE NOCASE ignore the case, ASC has to go last.

`Gorai.002G119600|Graimondii` - added  
`Gorai.008G038700|Graimondii` - added  
`Gorai.009G189500|Graimondii` - added  
`MDP0000126135` - Same as `MDP0000770493`  

---
**YnKn**

20 in file 21 in DB. 
`Gorai.008G030800|Graimondii` was missing  

---
**YnSKn**

121 in file 123 in DB

`Gorai.005G245900|Graimondii` - added  
`Gorai.012G154800|Graimondii` - added  


