tplx_dict = { 
'meta_docstring':'with the input code wrapped and framed',

'document_packages':r"""

    % define a code float
    \usepackage{newfloat} % to define a new float types
    \DeclareFloatingEnvironment[
        fileext=frm,placement={!ht},
        within=section,name=Code]{codecell}
    \DeclareFloatingEnvironment[
        fileext=frm,placement={!ht},
        within=section,name=Text]{textcell}
    \DeclareFloatingEnvironment[
        fileext=frm,placement={!ht},
        within=section,name=Text]{errorcell}
        
    \usepackage{listings} % a package for wrapping code in a box
    \usepackage[framemethod=tikz]{mdframed} % to fram code

""",

'document_header_end':r"""
% make the code float work with cleverref
\crefname{codecell}{code}{codes}
\Crefname{codecell}{code}{codes}
% make the text float work with cleverref
\crefname{textcell}{text}{texts}
\Crefname{textcell}{text}{texts}
% make the text float work with cleverref
\crefname{errorcell}{error}{errors}
\Crefname{errorcell}{error}{errors}
""",

'document_definitions':r"""
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.95}

\lstdefinestyle{mystyle}{
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily,
    breakatwhitespace=false,         
    keepspaces=true,                 
    numbers=left,                    
    numbersep=10pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2,
    breaklines=true,
    literate={\-}{}{0\discretionary{-}{}{-}},
  postbreak=\mbox{\textcolor{red}{$\hookrightarrow$}\space},
}
 
\lstset{style=mystyle} 

\surroundwithmdframed[
  hidealllines=true,
  backgroundcolor=backcolour,
  innerleftmargin=0pt,
  innerrightmargin=0pt,
  innertopmargin=0pt,
  innerbottommargin=0pt]{lstlisting}

""",

'notebook_input_code':r"""
((( draw_text(cell.metadata,cell.source,"code",
"language=Python,numbers=left,xleftmargin=20pt,xrightmargin=5pt,belowskip=5pt,aboveskip=5pt") )))
""",

'notebook_output_text':r"""
((( draw_text(cell.metadata,output.data['text/plain'],"text",
"language=Tex,numbers=none,xrightmargin=5pt") )))
""",

'notebook_output_stream':r"""
((( draw_text(cell.metadata,output.text | escape_latex | ansi2latex,"text",
              "language=Tex,numbers=none,xrightmargin=5pt,belowskip=2pt,aboveskip=2pt") )))
""",

'notebook_output_error':r"""
((( super() )))
""",
'notebook_output_traceback':"""
((( draw_text(cell.metadata,line | indent | strip_ansi | escape_latex,"error",
              "language=Python,numbers=none,xrightmargin=5pt,belowskip=2pt,aboveskip=2pt") )))
""",

'jinja_macros':r"""
((* macro draw_text(meta,source,type,options) -*))

((*- if meta.latex_doc: -*))

((*- if type in meta.latex_doc -*))

((*- if meta.latex_doc[type].asfloat: -*))
    ((*- if meta.latex_doc[type].placement: -*))
        ((*- if meta.latex_doc[type].widefigure: -*))
    \begin{(((type)))cell*}[((meta.latex_doc[type].placement)))]
        ((*- else -*))
    \begin{(((type)))cell}[(((meta.latex_doc[type].placement)))]
        ((*- endif *))
    ((*- else -*))
        ((*- if meta.latex_doc[type].widefigure: -*))
    \begin{(((type)))cell*}
        ((*- else -*))
    \begin{(((type)))cell}
        ((*- endif *))
    ((*- endif *))
    

    ((* set captionfound = false *))

    ((*- if meta.latex_doc[type].label: -*))
         ((*- if resources.captions: -*))
             ((*- if resources.captions[meta.latex_doc[type].label]: -*))
                 \caption{((( resources.captions[meta.latex_doc[type].label] )))}
                 ((* set captionfound = true *))
             ((*- endif *))
         ((*- endif *))
    ((*- endif *))


    ((*- if captionfound == false -*))
    ((*- if meta.latex_doc[type].caption: -*))
    \caption{((( meta.latex_doc[type].caption )))}
    ((*- endif *))
    ((*- endif *))

((*- endif *))

((*- if meta.latex_doc[type].label: -*))
\label{((( meta.latex_doc[type].label )))}
((*- endif *))

((*- if meta.latex_doc[type].format: -*))
\begin{lstlisting}[((( meta.latex_doc[type].format | dict_to_kwds(options) )))]
((*- else -*))
\begin{lstlisting}[((( options )))]
((*- endif *))
((( source )))
\end{lstlisting}

((*- if meta.latex_doc[type].asfloat: -*))
\end{(((type)))cell}
((*- endif *))

((*- endif *))

((*- endif *))
((*- endmacro *))
"""

}

