import React from "react";

import CloseIcon from '@mui/icons-material/Close';
import InfoIcon from '@mui/icons-material/Info';

import { Box, Dialog, DialogTitle, IconButton } from "@mui/material";


class DialogAlert extends React.Component {
    constructor(props) {
        super(props)
    }


    render() {
        return (
            <Dialog className='dialog-box' open={this.props.isOpen} onClose={this.handleClose}>
                <DialogTitle className="dialog-title"
                    sx={{
                        backgroundColor: this.props.colors.custom['bars'],
                        display: 'flex',
                        justifyContent: 'center',
                        alignItems: 'center',
                        border: '2px solid ',
                        borderColor: this.props.colors.blueAccent[100],
                        borderRadius: '3px 3px 0 0',
                        height: '60px',
                        color: this.props.colors.custom['barsIconsAndTexts']
                    }}
                >
                    <InfoIcon
                        sx={{
                            position: "absolute",
                            left: '20px',
                            color: this.props.colors.custom['barsIconsAndTexts']
                        }}
                    />
                    {this.props.title}
                    <IconButton
                        sx={{
                            position: 'absolute',
                            right: '20px',
                            color: this.props.colors.custom['barsIconsAndTexts']
                        }}
                        onClick={this.props.onClose}>
                        <CloseIcon />
                    </IconButton>
                </DialogTitle>

                <Box sx={{
                    backgroundColor: this.props.colors.primary[400],
                    display: 'flex',
                    justifyContent: 'center',
                    border: '2px solid ',
                    borderColor: this.props.colors.blueAccent[100],
                    borderRadius: ' 0 0 5px 5px',
                    borderTop: '0',
                    padding: '20px 15px',
                    color: this.props.colors.grey[300]

                }}>
                    {/* {this.props.body} */}
                    <p >Lorem ipsum dolor sit amet, consectetur adipisicing elit. Explicabo saepe harum,
                        voluptates laboriosam ut amet voluptatem nam voluptate, assumenda, repudiandae provident.
                        Accusamus voluptas distinctio culpa omnis aut in modi sequi.
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae doloremque,
                        architecto quod reiciendis quidem blanditiis quibusdam doloribus illo! Pariatur quibusdam qui
                        laborum aut totam error veritatis molestiae praesentium ratione alias?
                        <ul>
                            <li>Lorem ipsum dolor sit amet consectetur adipisicing elit.</li>
                            <li>laborum aut totam error veritatis molestiae praesentium ratione alias</li>
                            <li>Accusamus voluptas distinctio culpa omnis aut in modi sequi.F</li>
                        </ul>
                    </p>

                </Box>
            </Dialog>
        )
    }
}

export default DialogAlert