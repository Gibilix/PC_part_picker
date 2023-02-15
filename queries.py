#!/usr/bin/env python3

create_CPU_table = """
CREATE TABLE CPUs(
   CPU_Name    VARCHAR(20) NOT NULL PRIMARY KEY
  ,Price       INTEGER  NOT NULL
  ,Performance NUMERIC(11,8) NOT NULL
  ,TDP         INTEGER  NOT NULL
  ,iGPU        VARCHAR(1) NOT NULL
  ,PCores      INTEGER  NOT NULL
  ,ECores      INTEGER  NOT NULL
  ,Threads     INTEGER  NOT NULL
  ,OC          VARCHAR(1) NOT NULL
  ,DDR4        VARCHAR(1) NOT NULL
  ,DDR5        VARCHAR(1) NOT NULL
  ,Cooler      VARCHAR(1) NOT NULL
);
"""

insert_CPU = """
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('AMD Ryzen 5 5600',130,165.7,65,'N',6,0,12,'Y','Y','N','Y');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('Intel Core i3 13100',140,97.63571429,65,'Y',4,0,8,'N','Y','Y','Y');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('AMD Ryzen 5 5600X',160,137.0875,65,'N',6,0,12,'Y','Y','N','Y');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('Intel Core i5 12400',170,114.8529412,65,'Y',6,0,12,'N','Y','Y','Y');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('AMD Ryzen 7 5700G',170,144.7470588,65,'Y',8,0,16,'Y','Y','N','Y');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('AMD Ryzen 7 5700X',190,140.7210526,105,'N',8,0,16,'Y','Y','N','N');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('Intel Core i5 13400',220,120.35,65,'Y',6,4,16,'N','Y','Y','Y');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('AMD Ryzen 7 5800X',220,127.65,105,'N',8,0,16,'Y','Y','N','N');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('AMD Ryzen 5 7600',230,121.1565217,105,'Y',6,0,12,'Y','N','Y','Y');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('Intel Core i5 12600K',237,117.2320675,125,'Y',6,4,16,'Y','Y','Y','N');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('AMD Ryzen 5 7600X',244,117.6803279,105,'Y',6,0,12,'Y','N','Y','N');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('Intel Core i5 13600K',250,153.788,125,'Y',6,8,14,'Y','Y','Y','N');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('Intel Core i7 12700K',298,116.6208054,125,'Y',8,4,20,'Y','Y','Y','N');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('AMD Ryzen 7 5800X3D',300,92.9,105,'N',8,0,16,'N','Y','N','N');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('Intel Core i7 13700',320,123.928125,65,'Y',8,8,24,'N','Y','Y','Y');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('AMD Ryzen 7 7700',320,107.690625,65,'Y',8,0,16,'Y','N','Y','Y');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('AMD Ryzen 9 5900X',320,122.728125,105,'N',12,0,24,'Y','Y','N','N');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('Intel Core i7 13700K',330,142.2909091,133,'Y',8,8,24,'Y','Y','Y','N');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('AMD Ryzen 7 7700X',343,106.3061224,105,'Y',8,0,16,'Y','N','Y','N');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('Intel Core i9 12900K',415,100.1879518,125,'Y',8,8,20,'Y','Y','Y','N');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('Ryzen 9 7900X',418,124.5956938,170,'Y',12,0,24,'Y','N','Y','N');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('Ryzen 9 5950X',470,97.64042553,105,'N',16,0,32,'Y','Y','N','N');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('Intel Core i9 13900',520,97.625,65,'Y',8,16,32,'N','Y','Y','Y');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('Intel Core i9 13900K',530,113.2528302,125,'Y',8,16,32,'Y','Y','Y','N');
INSERT INTO CPUs(CPU_Name,Price,Performance,TDP,iGPU,PCores,ECores,Threads,OC,DDR4,DDR5,Cooler) VALUES ('AMD Ryzen 9 7950X',588,107.8537415,170,'Y',16,0,32,'Y','N','Y','N');
"""