package main

import (
	"fmt"
	"github.com/dikower/hack-starter/apps/users"
	"github.com/gofiber/fiber/v2"
	"log"
)

func main() {
	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) error {
		msg := fmt.Sprintf("Hello User! ✋ %s", c.Params("*"))
		return c.SendString(msg)
	})

	users.AddRoutes(app)
	log.Fatal(app.Listen(":8000"))
}
