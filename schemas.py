"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import date

# ---------------- HRMS Schemas ----------------

class Employee(BaseModel):
    """
    Employees collection schema
    Collection name: "employee"
    """
    first_name: str = Field(..., description="First name")
    last_name: str = Field(..., description="Last name")
    email: str = Field(..., description="Work email")
    phone: Optional[str] = Field(None, description="Phone number")
    department_id: Optional[str] = Field(None, description="Department ObjectId as string")
    role: Optional[str] = Field(None, description="Job title/role")
    hire_date: Optional[date] = Field(None, description="Hire date")
    status: Literal["active", "inactive"] = Field("active", description="Employment status")

class Department(BaseModel):
    """
    Departments collection schema
    Collection name: "department"
    """
    name: str = Field(..., description="Department name")
    description: Optional[str] = Field(None, description="Description")

class Leave(BaseModel):
    """
    Leave requests collection schema
    Collection name: "leave"
    """
    employee_id: str = Field(..., description="Employee ObjectId as string")
    start_date: date = Field(..., description="Start date")
    end_date: date = Field(..., description="End date")
    reason: Optional[str] = Field(None, description="Reason for leave")
    status: Literal["pending", "approved", "rejected"] = Field("pending", description="Approval status")

class Attendance(BaseModel):
    """
    Attendance events collection schema
    Collection name: "attendance"
    """
    employee_id: str = Field(..., description="Employee ObjectId as string")
    date: date = Field(..., description="Attendance date")
    type: Literal["checkin", "checkout"] = Field(..., description="Event type")
    note: Optional[str] = Field(None, description="Optional note")

# Example schemas (left for reference):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
