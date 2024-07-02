import { createContext, useState, useMemo } from 'react';
import { alpha, createStyles, createTheme } from '@mui/material/styles';
import { makeStyles } from '@mui/styles';

// Colors
export const tokens = (mode) => ({
    ...(mode === "dark"
        ? {
            grey: {
                100: "#e0e0e0",
                200: "#c2c2c2",
                300: "#a3a3a3",
                400: "#858585",
                500: "#666666",
                600: "#525252",
                700: "#3d3d3d",
                800: "#292929",
                900: "#141414",
                1100: "#737070", //Edit Page Color
            },
            primary: {
                100: "#d0d1d5",
                200: "#a1a4ab",
                300: "#727681",
                400: "#1F2A40",
                500: "#141b2d",
                600: "#101624",
                700: "#0c101b",
                800: "#080b12",
                900: "#040509",
            },
            greenAccent: {
                100: "#dbf5ee",
                200: "#b7ebde",
                300: "#94e2cd",
                400: "#70d8bd",
                500: "#4cceac",
                600: "#3da58a",
                700: "#2e7c67",
                800: "#1e5245",
                900: "#0f2922",
            },
            redAccent: {
                100: "#f8dcdb",
                200: "#f1b9b7",
                300: "#e99592",
                400: "#e2726e",
                500: "#db4f4a",
                600: "#af3f3b",
                700: "#832f2c",
                800: "#58201e",
                900: "#2c100f",
            },
            blueAccent: {
                100: "#e1e2fe",
                200: "#c3c6fd",
                300: "#a4a9fc",
                400: "#868dfb",
                500: "#6870fa",
                600: "#535ac8",
                700: "#3e4396",
                800: "#2a2d64",
                900: "#151632",
            },
            custom: {
                'barsIconsAndTexts': '#E7E7E7',
                'boxShadow': '#44444444',
                'headerTable': '#101624',
                'mainButton': '#0e3267',
                'secondaryButton': '#535ac8',
                'text': '#e0e0e0',
                'editableText': '#495057',
                'bars': '#1F2A40',
                'searchButtons': '#141b2d',
                'colorWhite': '#242526'
            }
        }
      : {
            grey: {
                100: "#141414",
                200: "#292929",
                300: "#3d3d3d",
                400: "#525252",
                500: "#666666",
                600: "#858585",
                700: "#a3a3a3",
                800: "#c2c2c2",
                900: "#e0e0e0",
                1100: "#616161", //Edit Page Color
            },
            primary: {
                100: "#040509",
                200: "#080b12",
                300: "#0c101b",
                400: "#f2f0f0",   
                500: "#141b2d",
                600: "#1F2A40",
                700: "#727681",
                800: "#a1a4ab",
                900: "#d0d1d5",
            },
            greenAccent: {
                100: "#0f2922",
                200: "#1e5245",
                300: "#2e7c67",
                400: "#3da58a",
                500: "#4cceac",
                600: "#70d8bd",
                700: "#94e2cd",
                800: "#b7ebde",
                900: "#dbf5ee",
            },
            redAccent: {
                100: "#2c100f",
                200: "#58201e",
                300: "#832f2c",
                400: "#af3f3b",
                500: "#db4f4a",
                600: "#e2726e",
                700: "#e99592",
                800: "#f1b9b7",
                900: "#f8dcdb",
            },
            blueAccent: {
                100: "#151632",
                200: "#2a2d64",
                300: "#3e4396",
                400: "#535ac8",
                500: "#6870fa",
                600: "#868dfb",
                700: "#a4a9fc",
                800: "#c3c6fd",
                900: "#e1e2fe",
                
            },
            custom: {
                'barsIconsAndTexts': '#E7E7E7',
                'boxShadow': '#44444444',
                'headerTable': '#0E3267',
                'mainButton': '#0e3267',
                'secondaryButton': '#EA5C11',
                'text': '#040F1F',
                'editableText': '#495057',
                'bars': '#0E3267',
                'searchButtons': '#0e3267',
                'colorWhite': '#ffffff'
            }
        }),
});

// Mui theme settings
export const themeSettings = (mode) => {
    const colors = tokens(mode)

    return {
        palette: {
            mode: mode,
            ...(mode === 'dark'
            ? {
                primary: {
                    main: colors.primary[500],
                    contrastText: colors.primary[100]
                },
                secondary: {
                    main: colors.blueAccent[500]
                },
                neutral: {
                    dark: colors.grey[700],
                    main: colors.grey[500],
                    light: colors.grey[100]
                },
                background: {
                    default: colors.primary[500]
                }
            } : {
                primary: {
                    main: colors.primary[100],
                    contrastText: colors.primary[900]
                },
                secondary: {
                    main: colors.blueAccent[500]
                },
                neutral: {
                    dark: colors.grey[700],
                    main: colors.grey[500],
                    light: colors.grey[100]
                },
                background: {
                    default: '#fcfcfc'
                }
            })
        },
        typography: {
            fontFamily: ['Montserrat', 'Source Sans 3', 'sans-serif'].join(','),
            fontSize: 12,
            h1: {
                fontFamily: ['Montserrat', 'Source Sans 3', 'sans-serif'].join(','),
                fontSize: 40
            },
            h2: {
                fontFamily: ['Montserrat', 'Source Sans 3', 'sans-serif'].join(','),
                fontSize: 32
            },
            h3: {
                fontFamily: ['Montserrat', 'Source Sans 3', 'sans-serif'].join(','),
                fontSize: 24
            },
            h4: {
                fontFamily: ['Montserrat', 'Source Sans 3', 'sans-serif'].join(','),
                fontSize: 20
            },
            h5: {
                fontFamily: ['Montserrat', 'Source Sans 3', 'sans-serif'].join(','),
                fontSize: 16
            },
            h6: {
                fontFamily: ['Montserrat', 'Source Sans 3', 'sans-serif'].join(','),
                fontSize: 14
            }
        }
    }
}

// Context for color mode
export const ColorModeContext = createContext({
    toggleColorMode: () => {}
})

export const useMode = () => {
    const [mode, setMode] = useState('light')

    const colorMode = useMemo(
        () => ({
            toggleColorMode: () => setMode((prev) => (prev === 'light' ? 'dark' : 'light'))
        })
    )

    const theme = useMemo(() => createTheme(themeSettings(mode)), [mode])

    return [theme, colorMode]
}

export const useStyles = makeStyles((theme) =>
  createStyles({
    root: {
      border: '1px solid #e2e2e1',
      overflow: 'hidden',
      borderRadius: 4,
      backgroundColor: '#fcfcfb',
      transition: theme.transitions.create(['border-color', 'box-shadow']),
      '&:hover': {
        backgroundColor: '#fff',
      },
      '&$focused': {
        backgroundColor: '#fff',
        boxShadow: `${alpha(theme.palette.primary.main, 0.25)} 0 0 0 2px`,
        borderColor: theme.palette.secondary.main,
      },
    },
    focused: {},
  }),
);