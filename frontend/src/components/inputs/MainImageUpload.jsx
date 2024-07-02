import React from "react";

import DeleteForeverIcon from '@mui/icons-material/DeleteForever';
import FileUploadIcon from '@mui/icons-material/FileUpload';

import { Box, IconButton, Typography } from "@mui/material";
import { displayImage } from "../../utils/file";
import { fileToHex } from "../../utils/file";

class MainImageUpload extends React.Component {
    constructor(props) {
        super(props);
        this.hiddenFileInput = React.createRef(); // Cria uma ref para o input de arquivo
    }

    deleteImage = (fieldName) => {
        this.props.handleChangeImage('', fieldName)
    }

    handleChange = (event) => {
        const fileUploaded = event.target.files[0];
        fileToHex(fileUploaded).then((hexString) => {
            this.props.handleChangeImage(hexString, event.target.id)
        })
      };

    uploadImage = () => {
        this.hiddenFileInput.current.click();
    }


    render() {
        return (
            <Box
                margin='auto'
                position='relative'
                width= 'fit-content'
                {...this.props}
            >
                {this.props.label ? 
                    <>
                        <Typography>{this.props.label}</Typography>
                    </>
                : <></>}
                <Box
                    id={this.props.id}
                    component='img'
                    src={this.props.src ? displayImage(this.props.src) : "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/User-avatar.svg/2048px-User-avatar.svg.png"}
                    margin='auto'
                    borderRadius='10px'
                    border='0.5px solid'
                    borderColor={this.props.colors.grey[1100]}
                    mt='10px'
                    maxHeight='200px'
                    height='fit-content'
                    width='100%'
                    maxWidth='300px'
                />
                <Box position='absolute' bottom='0' marginBottom='7px' borderRadius='10px' width='100%' display='flex' justifyContent='space-around'>
                    <Box backgroundColor='rgba(0,0,0,0.3)' width='50%' sx={{ cursor: 'pointer', borderBottomLeftRadius: '10px' }}>
                        <IconButton onClick={() => this.uploadImage()} sx={{ width: '100%' }}>
                            <FileUploadIcon sx={{ color: '#c2c2c2' }} />
                        </IconButton>
                        <input
                            id={this.props.id}
                            type="file"
                            ref={this.hiddenFileInput}
                            onChange={this.handleChange}
                            style={{ display: 'none' }}
                        />
                    </Box>
                    <Box backgroundColor='rgba(0,0,0,0.3)' width='50%' sx={{ cursor: 'pointer', borderBottomRightRadius: '10px' }}>
                        <IconButton onClick={() => this.deleteImage(this.props.id)} sx={{ width: '100%' }}>
                            <DeleteForeverIcon sx={{ color: '#c2c2c2' }} />
                        </IconButton>
                    </Box>
                </Box>
            </Box>
        )
    }
}

export default MainImageUpload;