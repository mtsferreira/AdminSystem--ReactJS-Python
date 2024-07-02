''' 

-- Step 0: Remove unique together
ALTER TABLE LocalEmail
DROP CONSTRAINT pk_LocalEmail

-- Step 1: Add a temp ID
ALTER TABLE LocalEmail
ADD IDLocalEmail INT IDENTITY(1,1);

-- Step 2: Drop the old primary key constraint, if it exists
IF EXISTS (SELECT * FROM sys.key_constraints WHERE type = 'PK' AND OBJECT_NAME(parent_object_id) = 'LocalEmail')
BEGIN
    ALTER TABLE LocalEmail DROP CONSTRAINT PK_LocalEmail; -- Replace PK_ProdutoMensagem with the actual primary key name
END

-- Step 4: Add the primary key constraint
ALTER TABLE LocalEmail
ADD CONSTRAINT PK_LocalEmail PRIMARY KEY (IDLocalEmail);


-- Step 6: Add Unique Together
ALTER TABLE LocalEmail
ADD CONSTRAINT UC_LocalEmail UNIQUE (IDLocal, IDTipoEmail);

''' 