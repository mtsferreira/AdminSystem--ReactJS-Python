''' 

-- Step 0: Remove unique together
ALTER TABLE ProdutoLocal
DROP CONSTRAINT pk_ProdutoLocal

-- Step 1: Add a temp ID
ALTER TABLE ProdutoLocal
ADD IDProdutoLocal INT IDENTITY(1,1);

-- Step 2: Drop the old primary key constraint, if it exists
IF EXISTS (SELECT * FROM sys.key_constraints WHERE type = 'PK' AND OBJECT_NAME(parent_object_id) = 'ProdutoLocal')
BEGIN
    ALTER TABLE ProdutoLocal DROP CONSTRAINT pk_ProdutoLocal; -- Replace PK_ProdutoMensagem with the actual primary key name
END

-- Step 3: Add the primary key constraint
ALTER TABLE ProdutoLocal
ADD CONSTRAINT pk_ProdutoLocal PRIMARY KEY (IDProdutoLocal);

-- Step 4: Add Unique Together
ALTER TABLE ProdutoLocal
ADD CONSTRAINT UC_ProdutoLocal UNIQUE (IDProduto, IDLocal);

'''