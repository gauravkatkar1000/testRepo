<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.Connection"%>
<%@page import ="java.sql.*" %>
<%@page import ="javax.sql.*" %>

<%
Class.forName("com.mysql.jdbc.Driver"); 
java.sql.Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/fci","root","31@dec2019"); 
Statement st= con.createStatement(); 
 Connection connection = null;
 Statement statement = null;
 ResultSet resultSet = null;
 String sql =""; 
 %>    
     
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Admin </title>
<style>
body {
  color: black;
  font-family: Calibri;
  font-size: 90%;
}

.btn-group button {
  background-color: #4CAF50 ; /* Green background #4CAF50*/
  border: 1px solid green; /* Green border */
  color: white; /* White text */
  padding: 5px 40px; /* Some padding */
  cursor: pointer; /* Pointer/hand icon */
  float: left; /* Float the buttons side by side */
}

/* Clear floats (clearfix hack) */
.btn-group:after {
  content: "";
  clear: both;
  display: table;
}

.btn-group button:not(:last-child) {
  border-right: none; /* Prevent double borders */
}

/* Add a background color on hover */
.btn-group button:hover {
  background-color: #3e8e41;
}

</style>

<script>
function f1()
{	
document.client_list_form.target = "rightframe";
document.client_list_form.action="Client_add.jsp";
document.client_list_form.submit();
}

function f2()
{	
//alert(document.role_list_form.radio_edit.value);
//alert('hiffff');
document.client_list_form.target = "rightframe";
document.client_list_form.action="Client_edit.jsp";
document.client_list_form.submit();}

function f3()
{	
var input_flag = confirm(" Confirm the Client which is going to delete : "+document.client_list_form.elements['edit_radio'].value);
	if(input_flag == true)
	{
		document.client_list_form.del_flag.value="Yes";
		document.client_list_form.target = "rightmidframe";
		document.client_list_form.action="Client_List.jsp";
		document.client_list_form.submit();
	}
}	

function f4()
{	
//alert(document.role_list_form.radio_edit.value);
//alert('hiffff');
document.client_list_form.target = "rightframe";
document.client_list_form.action="Client_user_map.jsp";
document.client_list_form.submit();}

</script>
</head>
<body style="font-size:15px">
<font style='font-family="Calibri"'>
<form name="client_list_form">
<input type="hidden" name="del_flag" value="">
<input type="hidden" name="client_name" value="">
<%
String del_flag=request.getParameter("del_flag");
String client_id = request.getParameter("edit_radio");
//out.println("del_flag"+del_flag+" client_id: "+client_id);
if (del_flag != null && del_flag.equals("Yes"))
{
 statement=con.createStatement(); 
 sql="DELETE FROM device_dtls WHERE device_id='"+client_id+"'"; 
 //out.println("sql  :"+sql); 
 statement.executeUpdate(sql);
 //connection.close();
 //out.println("User deleted sccessfully !!!!!!");
 }	
%>
<h3>  Clients </h3>   
<div class="btn-group">
  <button type="button" onclick="f1()"> Add Device</button> 
  <button type="button" onclick="f2()">Edit Device</button>  
  <button type="button" onclick="f3()">Delete Device</button>  
  <button type="button" onclick="f4()">User Device Mapping</button> 
</div>  
  <br> 
<table border=0 >
<tr bgcolor="grey" >
<td width="10%">Device ID</td>
<td width="20%">Description</td>
</tr>
<%
 try{
  statement=con.createStatement();
  sql ="SELECT device_id,device_id_str,company_name FROM device_dtls;";
  resultSet = statement.executeQuery(sql);
 while(resultSet.next()){
 %>
<tr>
<td><input type="radio" name="edit_radio" value="<%=resultSet.getString("device_id")%>"><%=resultSet.getString("device_id_str")%></td>
<td><%=resultSet.getString("company_name")%></td>
</tr>
<%
}
 connection.close();
 } catch (Exception e) {
 e.printStackTrace();
 }
%>
</table>


</form>
</font>
</body>
</html>