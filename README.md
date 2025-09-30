# 📦 Neighborhood Exchange Platform: Item Service

The **Item Service** is the foundational core component of the "Neighborhood Exchange Platform." Its sole responsibility is to manage the entire lifecycle of all user-posted **items** within the platform, from creation and viewing to updating and eventual delisting.

It exposes its functionality through a well-defined set of **RESTful APIs**, ensuring easy and reliable interaction for the front-end application and other microservices.

---

## ✨ Core Features (CRUD Operations)

This microservice implements the standard **CRUD** (Create, Read, Update, Delete) operations, which are the backbone of the platform's item management capabilities.

| Operation | HTTP Method | Endpoint | Description |
| :--- | :--- | :--- | :--- |
| **Create** | `POST` | `/items/` | Allows users to **list a new item**. |
| **Read (List)** | `GET` | `/items/` | Retrieves a **filterable list** of all active items. |
| **Read (Detail)** | `GET` | `/items/{item_id}` | Retrieves the **complete details** of a specific item. |
| **Update** | `PUT` | `/items/{item_id}` | Enables the item owner to **modify its details** (e.g., price, description). |
| **Delete** | `DELETE` | `/items/{item_id}` | Allows the owner to **delist** the item. |

---

## 💻 API Endpoints in Detail

### 1. Create Item (Listing an Item)

* **Endpoint:** `POST /items/`
* **Purpose:** To list a new item on the platform.
* **Requirements:** Essential information must be provided, including: `owner_id`, `title`, `transaction_type`, `condition`, and `location`.
* **System Action:** The system automatically assigns a **unique `id`** and records the creation timestamp.

### 2. View Item Details

* **Endpoint:** `GET /items/{item_id}`
* **Purpose:** To retrieve all data for a specific item, serving as the foundation for the platform's item detail pages.

### 3. Browse and Filter the Item List

* **Endpoint:** `GET /items/`
* **Purpose:** To retrieve a list of all currently active items.
* **Filtering:** This endpoint supports powerful, parameter-based filtering essential for community-based browsing:
    * **Filter by `location`:** Find items within a specific neighborhood or city.
    * **Filter by `owner_id`:** View all items listed by a particular user.
    * **Filter by `condition`:** Helps users find items that meet their quality expectations.

### 4. Update Item Information

* **Endpoint:** `PUT /items/{item_id}`
* **Purpose:** Allows the item's owner to modify details (e.g., update the price or description).
* **Note:** In a production environment, this endpoint would be protected by an authorization layer to ensure only the item's owner can perform this action.

### 5. Delete Item (Delisting)

* **Endpoint:** `DELETE /items/{item_id}`
* **Strategy:** We employ a **Soft Delete** strategy for data integrity and traceability.
* **Action:** Instead of permanent erasure, the item's status is marked as **`is_active = False`**. Delisted items are then hidden from standard browsing and search results.

---

## 🗄️ Data Model Highlights

The data structure uses **Pydantic models** for strict data validation, ensuring a robust and consistent data foundation.

* **`owner_id`:** A crucial link associating every item with a specific user.
* **`TransactionType` (Enum):** Strictly limits transaction types to `"Sale"`, `"Rent"`, `"Trade"`, or `"Free"`, ensuring business logic consistency.
* **`ItemCondition` (Enum):** Standardizes the item's condition (e.g., `"New"`, `"Like New"`, `"Used"`).
* **Price and Transaction Logic:** The `price` field is designed to be **optional** and is logically relevant only for `"Sale"` or `"Rent"` items, enhancing model robustness.
