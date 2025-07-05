import streamlit as st
import sqlite3
import pandas as pd

# SQLite Database Application with Streamlit
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        st.error(f"Error connecting to database: {e}")
        return None
    
def create_table(conn):
    """Create a table in the SQLite database."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                country TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Error creating table: {e}")

def insert_user(conn, name, email, country):
    """Insert a new user into the users table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (name, email, country)
            VALUES (?, ?, ?)
        ''', (name, email, country))
        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Error inserting user: {e}")

def fetch_users(conn):
    """Fetch all users from the users table."""
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        return pd.DataFrame(rows, columns=['ID', 'Name', 'Email', 'Country'])
    except sqlite3.Error as e:
        st.error(f"Error fetching users: {e}")
        return pd.DataFrame(columns=['ID', 'Name', 'Email', 'Country'])

def edit_user(conn, user_id, name, email, country):
    """Edit an existing user in the users table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE users
            SET name = ?, email = ?, country = ?
            WHERE id = ?
        ''', (name, email, country, user_id))
        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Error updating user: {e}")

def delete_user(conn, user_id):
    """Delete a user from the users table."""
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Error deleting user: {e}")

# Main function to run the Streamlit application

def main():
    st.title("SQLite Database Application")
    
    # Connect to the database
    conn = create_connection("users.db")
    if conn is None:
        st.stop()
    
    # Create the users table if it doesn't exist
    create_table(conn)
    
    # User input form
    name = st.text_input("Name")
    email = st.text_input("Email")
    country = st.text_input("Country")
    
    # Insert user into the database
    if st.button("Add User"):
        if '@' not in email or '.' not in email.split('@')[-1]:
            st.error("Please enter a valid email address.")
            st.stop()
        else:  
            st.success("Email address is valid.")

        insert_user(conn, name, email, country)
        st.success("User added successfully!")
        st.balloons()
    
    # Fetch and display users from the database
    users_df = fetch_users(conn)
    st.dataframe(users_df)

    # Edit user functionality
    if not users_df.empty:
        user_id = st.selectbox("Select User to Edit", users_df['ID'])
        selected_user = users_df[users_df['ID'] == user_id].iloc[0]
        
        edit_name = st.text_input("Edit Name", value=selected_user['Name'])
        edit_email = st.text_input("Edit Email", value=selected_user['Email'])         
        edit_country = st.text_input("Edit Country", value=selected_user['Country'])
        
        if st.button("Update User"):
            if '@' not in edit_email or '.' not in edit_email.split('@')[-1]:
                st.error("Please enter a valid email address.")
                st.stop()
            else:  
                st.success("Email address is valid.")            
            edit_user(conn, user_id, edit_name, edit_email, edit_country)
            st.success("User updated successfully!")
            st.balloons()
    
    # Delete user functionality
    if not users_df.empty:
        delete_user_id = st.selectbox("Select User to Delete", users_df['ID'])
        if st.button("Delete User"):
            delete_user(conn, delete_user_id)
            st.success("User deleted successfully!")
            st.balloons()

    # Close the database connection
    conn.close()
if __name__ == "__main__":
    main()
    #st.set_page_config(page_title="SQLite DB App", layout="wide")
