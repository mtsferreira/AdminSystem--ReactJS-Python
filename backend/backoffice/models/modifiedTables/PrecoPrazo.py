''''
-- Step 0: Remove unique together
ALTER TABLE PrecoPrazo
DROP CONSTRAINT pk_PrecoPrazo

-- Step 1: Add a temp ID
ALTER TABLE PrecoPrazo
ADD IDPrecoPrazo INT IDENTITY(1,1);

-- Step 2: Drop the old primary key constraint, if it exists
IF EXISTS (SELECT * FROM sys.key_constraints WHERE type = 'PK' AND OBJECT_NAME(parent_object_id) = 'PrecoPrazo')
BEGIN
    ALTER TABLE PrecoPrazo DROP CONSTRAINT pk_PrecoPrazo; -- Replace PK_ProdutoMensagem with the actual primary key name
END

-- Step 3: Add the primary key constraint
ALTER TABLE PrecoPrazo
ADD CONSTRAINT pk_PrecoPrazo PRIMARY KEY (IDPrecoPrazo);

-- Step 4: Add Unique Together
ALTER TABLE PrecoPrazo
ADD CONSTRAINT UC_PrecoPrazo UNIQUE (IDPreco, PrazoDias);
'''