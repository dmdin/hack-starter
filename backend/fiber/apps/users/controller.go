package users

import (
	"github.com/gofiber/fiber/v2"
)

func AddRoutes(app fiber.Router) {
	r := app.Group("/users")
	r.Get("/", func(ctx *fiber.Ctx) error {
		return ctx.SendString("Hello user!")
	})
}
