graphs.py
=========

.. py:class:: Graph

   Построение графа

   :var gr_CommonFr: Граф, показывающий как много общих друзей между пользователем и его друзьями 
   :var gr_Group: Граф, показывающий как много друзей пользователя являются участниками определенного количества тех или иных его групп
   :var gr_GroupSix: Граф, показывающий как много друзей пользователя являются участниками определенных групп
   :var friends: Друзья определённого пользователя
   :var last_add: Объекты, которые будут добавлены в граф **gr_CommonFr** при его изменении
   :var pers_obj: Объект класса :py:class:`Profile`
   :var api: Сессия VK
   :var token: Токен

   .. py:method:: __init__(pers_obj, api, token)

      Конструктор

      :param pers_obj: Ссылка на пользователя VK
      :param api: Сессия VK
      :param token: Токен

   .. py:method:: onClick(event)

      Функция для поиска друзей определенного пользователя

      :param event: Событие, при котором начинается выполнение данной функции 

   .. py:method:: make_friendsGraph(common_friends)

      Функция для создания графа **gr_CommonFr**

      :param common_friends: Масссив, содержащий в себе информацию для построения вершин и веток 

   .. py:method:: show_friendsGraph()

      Функция для рисования графа **gr_CommonFr**

   .. py:method:: make_groupGraph(fname, lname, personal_card)

      Функция для создания графа **gr_Group**

      :param fname: Имя пользователя, для которого создается граф
      :param lname: Фамилия пользователя, для которого создается граф
      :param personal_card: Масссив, содержащий в себе информацию для построения вершин и веток

   .. py:method:: show_groupGraph()

      Функция для рисования графа **gr_Group**

   .. py:method:: make_groupGraphSix(fname, lname, personal_card)

      Функция для создания графа **gr_GroupSix**

      :param fname: Имя пользователя, для которого создается граф
      :param lname: Фамилия пользователя, для которого создается граф
      :param personal_card: Масссив, содержащий в себе информацию для построения вершин и веток

   .. py:method:: show_groupGraphSix()

      Функция для рисования графа **gr_GroupSix**


