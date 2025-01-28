import React, { useState } from 'react';  

const SuperuserConsole = () => {  
  const [command, setCommand] = useState('');  
    const [output, setOutput] = useState('');  

      const handleCommand = async () => {  
          const res = await fetch('/api/execute', {  
                method: 'POST',  
                      body: JSON.stringify({ command }),  
                          });  
                              setOutput(await res.text());  
                                };  

                                  return (  
                                      <div className="console">  
                                            <input  
                                                    type="text"  
                                                            value={command}  
                                                                    onChange={(e) => setCommand(e.target.value)}  
                                                                            placeholder="Wpisz komendę SUPERUSER..."  
                                                                                  />  
                                                                                        <button onClick={handleCommand}>▶ Wykonaj</button>  
                                                                                              <pre>{output}</pre>  
                                                                                                  </div>  
                                                                                                    );  
                                                                                                    };  

                                                                                                    export default SuperuserConsole;  