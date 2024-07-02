'''
-- Step 1: Add a temp ID
ALTER TABLE TempCarteiraPedido
ADD IDCarteiraPedido INT IDENTITY(1,1) NOT NULL;

-- Step 4: Add the primary key constraint
ALTER TABLE TempCarteiraPedido
ADD CONSTRAINT PK_CarteiraPedido PRIMARY KEY (IDCarteiraPedido);
'''