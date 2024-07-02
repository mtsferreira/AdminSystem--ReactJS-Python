'''
ALTER TABLE RepresentadaLocal
DROP CONSTRAINT pk_RepresentadaLocal

-- Step 1: Add a temp ID
ALTER TABLE RepresentadaLocal
ADD IDRepresentadaLocal INT IDENTITY(1,1);

-- Step 2: Drop the old primary key constraint, if it exists
IF EXISTS (SELECT * FROM sys.key_constraints WHERE type = 'PK' AND OBJECT_NAME(parent_object_id) = 'RepresentadaLocal')
BEGIN
    ALTER TABLE RepresentadaLocal DROP CONSTRAINT PK_RepresentadaLocal; -- Replace PK_ProdutoMensagem with the actual primary key name
END

-- Step 3: Add the primary key constraint
ALTER TABLE RepresentadaLocal
ADD CONSTRAINT PK_RepresentadaLocal PRIMARY KEY (IDRepresentadaLocal);

-- Step 4: Add Unique Together
ALTER TABLE RepresentadaLocal
ADD CONSTRAINT UC_RepresentadaLocal UNIQUE (IDRepresentada, IDLocal);'
'''