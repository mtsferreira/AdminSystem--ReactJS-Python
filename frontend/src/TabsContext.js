import React, { createContext, useContext, useState } from 'react';

// Criação do contexto
export const TabsContext = createContext();

// Componente provedor
export const TabsProvider = ({ children }) => {
   const [tabs, setTabs] = useState([]); // Armazena as abas abertas
   const [activeTab, setActiveTab] = useState(null); // Aba ativa atual

   // Função para abrir uma nova aba
   const openTab = (tab) => {
      // Verifica se a aba já está aberta
      const existing = tabs.find((t) => t.key === tab.key);
      if (!existing) {
         setTabs([...tabs, tab]);
      }
      setActiveTab(tab.key);
   };

   // Função para mudar a aba ativa
   const switchTab = (tabKey) => {
      setActiveTab(tabKey);
   };

   // Função para fechar uma aba
   const closeTab = (tabKey) => {
      setTabs(tabs.filter((tab) => tab.key !== tabKey));
      if (activeTab === tabKey) {
         setActiveTab(null);
      }
   };

   return (
      <TabsContext.Provider value={{ tabs, activeTab, openTab, switchTab, closeTab }}>
         {children}
      </TabsContext.Provider>
   );
};

// Hook personalizado para usar o contexto de abas
export const useTabs = () => useContext(TabsContext);